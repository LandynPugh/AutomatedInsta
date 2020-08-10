import sqlite3
from post import Post
from os.path import isfile

def create_db(dir):
    #ARGUMENTS: dir = the directory in which the database will be created.
    #create_db creates the database used to store the captions and images
    conn = sqlite3.connect(dir)
    c = conn.cursor()
    c.execute("""CREATE TABLE posts (
                id integer,
                image text,
                caption text
                )""")
    conn.commit()
    conn.close()

def check_ifDb(dir):
    #ARGUMENTS: dir = the directory in which the database will be created.
    #check_ifDb checks if the database exists.
    #If not, it creates it.
    if isfile(dir):
        print('Database in directory!')
    else:
        f = open(dir, 'x')
        f.close()
        create_db(dir)

def send_Deets(post):
    #ARGUMENTS: post = instance of the Post class.
    #Adds post image and caption from a given instance of Post to the database
    conn = sqlite3.connect('./posts/post_record.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM posts")
    id = c.fetchone()[0]
    print(id)
    c.execute("INSERT INTO posts VALUES (?, ?, ?)", (id, post.image, post.caption))
    conn.commit()
    conn.close()

def grab_Deets():
    #RETURNS: An instance of the Post class containing the first image and caption added (id = 0)
    conn = sqlite3.connect('./posts/post_record.db')
    c = conn.cursor()
    c.execute("SELECT image FROM posts WHERE id = :id", {'id': 0})
    currentImage = c.fetchall()[0][0]
    c.execute("SELECT caption FROM posts WHERE id = :id", {'id': 0})
    currentCapt = c.fetchall()[0][0]
    currentPost = Post(currentImage, currentCapt)

    c.execute("DELETE FROM posts WHERE id = :id", {'id': 0})
    conn.commit()

    c.execute("SELECT COUNT(*) FROM posts")
    dbThiccness= c.fetchone()[0]
    print(dbThiccness)
    for bird in range(dbThiccness):
        c.execute("UPDATE posts SET id = :newid WHERE id = :oldid", {'newid': bird, 'oldid': bird+1})

    conn.commit()
    conn.close()
    return currentPost



if __name__ == '__main__':
    #Only called if database.py is run through the interpreter
    #Creates "post_record.db" if it does not already exist
    check_ifDb('./posts/post_record.db')
    conn = sqlite3.connect('./posts/post_record.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    conn.close()
