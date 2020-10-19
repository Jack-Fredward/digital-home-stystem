#study.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class study:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Study Lights",dbCursor)
        self.lights.actuators.append(actuator("Study Light Actuator","Study Lights",dbCursor))
        self.lights.sensors.append(brightSensor("SLBS","Study Lights", dbCursor))
        self.lights.sensors.append(motionSensor("SLMS","Study Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = device("Study door", dbCursor)
        self.doors.append(device("Study door",dbCursor))
        self.doors.actuators.append(actuator("Study Door Actuator", "Study door",dbCursor))
        self.doors.sensors.append(openCloseSensors("SDOCS","HBathroom door",dbCursor))
       

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = device("Study window",dbCursor)
        self.windows.append(device("Study window",dbCursor))
        self.windows.actuators.append(actuator("Study window Actuator", "Study window",dbCursor))
        self.windows.sensors.append(openCloseSensors("SWOCS","Study window",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("SATS","Air",dbCursor))
        self.air.actuators.append(actuator("Study Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        self.cameras = device("Study Camera",dbCursor)
        self.cameras.append(device("Study Camera",dbCursor))
        self.cameras.actuators.append(actuator("Study Camera Actuator","Study Camera",dbCursor))
        self.cameras.sensors.append(motionSensor("SCMS","Study Camera",dbCursor))

        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Study Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("SSS","Study Alarm", dbCursor))


    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DOORS
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

    #-------------------------------------------------------------
    #   SMOKE ALARM
    #-------------------------------------------------------------