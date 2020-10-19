#dining_room.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class Dining_Room:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Dining_Room Lights",dbCursor)
        self.lights.actuators.append(actuator("Dining_Room Light Actuator","Dining_Room Lights",dbCursor))
        self.lights.sensors.append(brightSensor("DRLBS","Dining_Room Lights", dbCursor))
        self.lights.sensors.append(motionSensor("DRLMS","Dining_Room Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        #   NO DOORS

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = device("Dining_Room window",dbCursor)
        self.windows.append(device("Dining_Room window",dbCursor))
        self.windows.actuators.append(actuator("Dining_Room window Actuator", "Dining_Room window",dbCursor))
        self.windows.sensors.append(openCloseSensors("DRWOCS","Dining_Room window",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("DRATS","Air",dbCursor))
        self.air.actuators.append(actuator("Dining_Room Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        self.cameras = device("Dining_Room Camera",dbCursor)
        self.cameras.append(device("Dining_Room Camera",dbCursor))
        self.cameras.actuators.append(actuator("Dining_Room Camera Actuator","Dining_Room Camera",dbCursor))
        self.cameras.sensors.append(motionSensor("DRCMS","Dining_Room Camera",dbCursor))

        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Dining_Room Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("DRSS","Dining_Room Alarm", dbCursor))


    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DOORS
    #-------------------------------------------------------------

    # NO DOORS

    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   CAMERAS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   SMOKE ALARM
    #-------------------------------------------------------------