#Robert's_bedroom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class Robert_bedroom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Robert's bedRoom Lights",dbCursor)
        self.lights.actuators.append(actuator("Robert's bedRoom Light Actuator","Robert's bedRoom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("RBLBS","Robert's bedRoom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("RBLMS","Robert's bedRoom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("RBinteriordoor",dbCursor))
        self.doors[0].actuators.append(actuator(" Robert's bedRoom Interior Door Actuator", "RBinteriodoor",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("RBIDOCS","RBinteriordoor",dbCursor))
        
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("RBATS","Air",dbCursor))
        self.air.actuators.append(actuator("Robert's bedRoom Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        
        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Smoke Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("RBSS","Smoke Alarm", dbCursor))


    #-------------------------------------------------------------
    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   CAMERAS
    #-------------------------------------------------------------


  
