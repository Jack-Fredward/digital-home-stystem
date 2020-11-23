import pymysql
from device import *
import datetime

class mainDoor:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #-------------------------------------------------------------
        self.mainDoor = device("Main Door",dbCursor)
        self.mainDoor.actuators.append(actuator("Main Door Actuator","Main Door", dbCursor))
        self.mainDoor.sensors.append(openCloseSensors("MDOCS", "Main Door",dbCursor))
        #-------------------------------------------------------------
        #   METHODS
        #-------------------------------------------------------------
        #-------------------------------------------------------------
        #   DOORS
        #-------------------------------------------------------------

    def openDoor(self,frame,db):
        self.mainDoor.actuators[0].turnOn()
        self.mainDoor.sensors[0].updateOpen()
        frame.doorStateDisplayLabel.config(text="Open")
        frame.update()
        db.commit()

    def closeDoor(self,frame,db):
        self.mainDoor.actuators[0].turnOff()
        self.mainDoor.sensors[0].updateClosed()
        frame.doorStateDisplayLabel.config(text="Closed")
        frame.update()
        db.commit()

    def getDoorState(self,doorNum):
        return self.mainDoor.actuators[0].getState()

    def getDoorOpenCloseState(self,doorNum):
        return self.mainDoor.sensors[0].getState()

    def getName(self):
        return self.name
