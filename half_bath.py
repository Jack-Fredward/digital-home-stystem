#Half_Bath.py


import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class Hbathroom:
    def __init__(self, name, number, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("HBathroom Lights",dbCursor)
        self.lights.actuators.append(actuator("HBathroom Light Actuator","HBathroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("HBLBS","HBathroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("HBLMS","HBathroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = device("HBathroom door", dbCursor)
        self.doors.append(device("HBathroom door",dbCursor))
        self.doors.actuators.append(actuator("HBathroom Door Actuator", "HBathroom door",dbCursor))
        self.doors.sensors.append(openCloseSensors("HBDOCS","HBathroom door",dbCursor))

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        # NO WINDOWS

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("HBATS","Air",dbCursor))
        self.air.actuators.append(actuator("HBathroom Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("HBathroom Sink", dbCursor)
        self.sink.actuators.append(actuator("HBathroom Sink Actuator","HBathroom Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("HBSLFS","HBathroom Sink",dbCursor))
       
     
        #-------------------------------------------------------------
        #   TOILET
        #-------------------------------------------------------------
        
        self.toilet = device("HBathroom Toilet", dbCursor)
        self.toilet.actuators.append(actuator("HBathroom Toilet Actuator","HBathroom Toilet",dbCursor))
        self.toilet.sensors.append(liquidFlowSensor("HBTLFS","HBathroom Toilet",dbCursor))



    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DOORS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------
    
    #-------------------------------------------------------------
    #   TOILET
    #-------------------------------------------------------------