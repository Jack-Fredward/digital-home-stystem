import pymysql
from kitchen import *
import datetime
import time

def simMainDoor(db, frame, mainDoor, code):
    if code == 1234:
        mainDoor.openDoor(frame,db)