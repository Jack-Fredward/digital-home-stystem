#breakfast_nook.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class breakfast_nook:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Breakfast_Nook Lights",dbCursor)
        self.lights.actuators.append(actuator("Breakfast_Nook Light Actuator","Breakfast_Nook Lights",dbCursor))
        self.lights.sensors.append(brightSensor("BNLBS","Breakfast_Nook Lights", dbCursor))
        self.lights.sensors.append(motionSensor("BNLMS","Breakfast_Nook Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        #   NO DOORS

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = device("Breakfast_Nook window",dbCursor)
        self.windows.append(device("Breakfast_Nook window",dbCursor))
        self.windows.actuators.append(actuator("Breakfast_Nook window Actuator", "Breakfast_Nook window",dbCursor))
        self.windows.sensors.append(openCloseSensors("BNWOCS","Breakfast_Nook window",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("BNATS","Air",dbCursor))
        self.air.actuators.append(actuator("Breakfast_Nook Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        self.cameras = device("Breakfast_Nook Camera",dbCursor)
        self.cameras.append(device("Breakfast_Nook Camera",dbCursor))
        self.cameras.actuators.append(actuator("Breakfast_Nook Camera Actuator","Breakfast_Nook Camera",dbCursor))
        self.cameras.sensors.append(motionSensor("BNCMS","Breakfast_Nook Camera",dbCursor))

        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Breakfast_Nook Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("BNSS","Breakfast_Nook Alarm", dbCursor))


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