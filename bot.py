from instabot import Bot
from database import grab_Deets
from os import remove
from PIL import Image
from post import Post
from os import remove

if __name__ == '__main__':

    #Openining login.txt to recieve username and password
    with open('login.txt', 'r') as credentials:
        username = credentials.readline().split(': ')[1].rstrip()
        password = credentials.readline().split(': ')[1].rstrip()

    #Creating instance of "Post" and grabbing a post from the database
    freeBird = Post("temp", "temp")
    freeBird = grab_Deets()

    #Posting the recieved post and removing the image afterwards
    bot = Bot()
    bot.login(username = username, password = password, ask_for_code=True)
    bot.upload_photo(freeBird.image, freeBird.caption)
    remove(freeBird.image + ".REMOVE_ME")
