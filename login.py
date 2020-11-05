#login3

import logging
import bcrypt
import pymysql
import time


logging.basicConfig(level=logging.DEBUG)


def check_password(user_id, password):
    hashed = get_password_hash(user_id)
    if bcrypt.checkpw(password.encode('utf8'), hashed):
        logging.debug(f"password for user {user_id} matches")
        return True
    else:
        logging.debug(f"password for user {user_id} does not match")
        return False

def get_password_hash(user_id):
    # Open database connection
    # db = pymysql.connect("localhost","root","","digital_home_database" )
    db = pymysql.connect("localhost","jp","Database","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute(f"SELECT pw_hash FROM Users WHERE U_ID = {user_id};")
    pw_hash = cursor.fetchall()[0][0]
    db.close()
    # print(pw_hash)
    return pw_hash

def get_user_id_from_user_fn(user_fn):
    # Open database connection
    # db = pymysql.connect("localhost","root","","digital_home_database" )
    db = pymysql.connect("localhost","jp","Database","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # user_id = cursor.execute(f"SELECT U_ID FROM Users WHERE F_Name = {user_fn};")
    cursor.execute("SELECT U_ID FROM Users WHERE F_Name = '"+str(user_fn)+"';")
    user_id = cursor.fetchall()[0][0]
    # print(user_id)
    db.close()
    return user_id

def login(user_fn, password,controller,MainMenu):
    user_id = get_user_id_from_user_fn(user_fn)
    if check_password(user_id, password):
        controller.show_frame(MainMenu)
    else:
        print("Wrong username or password")


def hash_pw(user_fn, password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)
    db = pymysql.connect("localhost","jp","Database","digital_home_database" )
    cursor = db.cursor()

    # print(hashed)
    # print(str(hashed)[1:])
    # print("UPDATE Users SET pw_hash="+str(hashed)[1:]+" WHERE F_Name = '"+str(user_fn)+"';")

    cursor.execute("UPDATE Users SET pw_hash="+str(hashed)[1:]+" WHERE F_Name = '"+str(user_fn)+"';")
    db.commit()
    db.close()

def update_pw(frame, user_fn, password,controller,LoginPage):
    hash_pw(user_fn, password)
    frame.passwordUpdateLabel.config(text = "Password Successfully updated")
    frame.update()
    time.sleep(3)
    controller.show_frame(LoginPage)
    
    


# def main():
#     # hash_pw("Steve", "password")

#     if login("Steve","password"):
#         print("Good Login")
#     else:
#         print("Denied")

# main()




# def login(username, password,controller,MainMenu):
#     if(username == "test" and password == "test"):
#         #print("All good")
#         controller.show_frame(MainMenu)
#     else:
#         print("Wrong username or password")