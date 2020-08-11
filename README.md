# Automated Instagram

Automated Instagram is a collection of scripts that together, simplify the automatic uploading of images and captions to a given instagram account feed.

## Scripts

- dir_watch.py
    - Keeps track of files added to .\posts\pictures
- bot.py
    - Runs the bot that posts images and captions from the database to the chosen account's feed

## Required modules:
- [instabot 0.117.0](https://github.com/mastizada/instabot)
- [watchdog 0.10.3](https://github.com/gorakhargosh/watchdog)

### Installation

Automated Instagram requires python 3.0, [instabot 0.117.0](https://github.com/mastizada/instabot/) and [watchdog 0.10.3](https://github.com/gorakhargosh/watchdog) to run.

Before running scripts, enter the username and password of your chosen instagram account into "login.txt" and enter a list of captions into "captions.txt" within the "posts" folder. Ensure that each caption is separated by a newline character.
| :warning:  The data entered into this file is processed by Instabot. This is an external module. It is not reccomended to give the password of any account containing personal or important information.  |
|-----------------------------------------|

If dependencies are to be installed using a virtual environment, name the environment folder "venv", you will be able to run "directory_watch.bat", which in turn runs "dir_watch.py". With this script running, you will be able to move any images you want to be uploaded into the "posts\pictures" directory.
Now every time "insta_post.bat" is run, the first image added to the "posts\pictures" folder will be uploaded to your account along with the first caption in "captions.txt".

### IF DEPENDENCIES ARE NOT INSTALLED USING A VIRTUAL ENVIRONMENT

- Open directory_watch.bat and insta_post.bat in a plain text editor and remove the following text from both: <br>
```bash
.\venv\Scripts\activate&&
```

### Running the First Time
The first time insta_post.bat is run, you will be asked by the terminal to enter a verification code. This code will be accessible through the email address associated with the instagram account.

### Todos

 - Add auto-cropping images
 - Possible automatic respond-to-messages?

License
----

MIT



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
