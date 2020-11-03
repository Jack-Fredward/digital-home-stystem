#login3

import logging
import bcrypt
import pymysql


logging.basicConfig(level=logging.DEBUG)


def check_password(user_id, password):
    hashed = get_password_hash(user_id)
    if bcrypt.checkpw(password, hashed):
        logging.debug(f"password for user {user_id} matches")
        return True
    else:
        logging.debug(f"password for user {user_id} does not match")
        return True

def get_password_hash(user_id):
    # Open database connection
    db = pymysql.connect("localhost","root","","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    pw_hash = cursor.execute(f"SELECT pw_hash FROM Users WHERE U_ID = {user_id};")
    return pw_hash

def get_user_id_from_user_fn(user_fn):
    # Open database connection
    db = pymysql.connect("localhost","root","","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    user_id = cursor.execute(f"SELECT U_ID FROM Users WHERE F_Name = {user_fn};")
    return user_id

def login(user_fn, password):
    user_id = get_user_id_from_user_fn(user_fn)
    if check_password(user_id, password):
        return True
    else:
        return False
