import time
from os.path import getsize
import database
from post import Post
from random import randint
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
    if "REMOVE_ME" not in event.src_path:
        captionSize = getsize("./posts/captions.txt")
        image = event.src_path
        with open("./posts/captions.txt", "r+") as captionFile:
            if captionSize == 0:
                randomCapt = [<ENTER CAPTION OF CHOICE>] #List of strings containing default captions in the case that captions.txt is empty.
                randIndex = randint(0, len(randomCapt)-1)
                chosenCaption = randomCapt[randIndex]
            else:
                captions = captionFile.readlines()
                #randIndex = randint(0, len(captions)-1) <- turn off comments and replace
                #0 in "pop" method below with "randIndex" to allow for a random caption to be selected
                chosenCaption = captions.pop(0)
                captionFile.truncate(0)
                captionFile.seek(0)
                captionFile.writelines(captions)
                currentPost = Post(image, chosenCaption.strip())
                database.send_Deets(currentPost)

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created

    path = "./posts/pictures"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive = go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
