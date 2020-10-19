#bathroom1.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class bathroom:
    def __init__(self, name, number, dbCursor, has_shower, has_bathtub, has_extDoor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Bathroom"+number+"Lights",dbCursor)
        self.lights.actuators.append(actuator("Bathroom"+number+"Light Actuator","Bathroom"+number+"Lights",dbCursor))
        self.lights.sensors.append(brightSensor("B"+number+"LBS","Bathroom"+number+"Lights", dbCursor))
        self.lights.sensors.append(motionSensor("B"+number+"LMS","Bathroom"+number+"Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("Bathroom"+number+"door",dbCursor))
        self.doors[0].actuators.append(actuator("Bathroom"+number+"Door Actuator", "Bathroom"+number+"door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("B"+number+"DOCS","Bathroom"+number+"door",dbCursor))

        if (has_extDoor == 1):
            self.doors.append(device("Bathroom"+number+"ExtDoor",dbCursor))
            self.doors.actuators.append(actuator("Bathroom"+number+"ExtDoor Actuator", "Bathroom"+number+"ExtDoor",dbCursor))
            self.doors.sensors.append(openCloseSensors("B"+number+"EDOCS","Bathroom"+number+"ExtDoor",dbCursor))
      
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = device("Bathroom"+number+"window",dbCursor)
        self.windows.append(device("Bathroom"+number+"window",dbCursor))
        self.windows.actuators.append(actuator("Bathroom"+number+"window Actuator", "Bathroom"+number+"window",dbCursor))
        self.windows.sensors.append(openCloseSensors("B"+number+"WOCS","Bathroom"+number+"window",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("B"+number+"ATS","Air",dbCursor))
        self.air.actuators.append(actuator("Bathroom"+number+"Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("Bathroom"+number+"Sink", dbCursor)
        self.sink.actuators.append(actuator("Bathroom"+number+"Sink Actuator","Bathroom"+number+"Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("B"+number+"SLFS","Bathroom"+number+"Sink",dbCursor))
       
        #-------------------------------------------------------------
        #   TOILET
        #-------------------------------------------------------------
        
        self.toilet = device("Bathroom"+number+"Toilet", dbCursor)
        self.toilet.actuators.append(actuator("Bathroom"+number+"Toilet Actuator","Bathroom"+number+"Toilet",dbCursor))
        self.toilet.sensors.append(liquidFlowSensor("B"+number+"TLFS","Bathroom"+number+"Toilet",dbCursor))

        #-------------------------------------------------------------
        #   SHOWER
        #-------------------------------------------------------------

        if (has_shower == 1):
            self.shower = device("Bathroom"+number+"shower",dbCursor)
            self.shower = device("Bathroom"+number+"Shower", dbCursor)
            self.shower.actuators.append(actuator("Bathroom"+number+"Shower Actuator","Bathroom"+number+"Shower",dbCursor))
            self.shower.sensors.append(liquidFlowSensor("B"+number+"SHLFS","Bathroom"+number+"Shower",dbCursor))
        #-------------------------------------------------------------
        #   BATHTUB
        #-------------------------------------------------------------
        
        if (has_bathtub == 1):
            self.bathtub = device("Bathroom"+number+"bathtub",dbCursor)
            self.bathtub = device("Bathroom"+number+"bathtub", dbCursor)
            self.bathtub.actuators.append(actuator("Bathroom"+number+"Bathtub Actuator","Bathroom"+number+"Bathtub",dbCursor))
            self.bathtub.sensors.append(liquidFlowSensor("B"+number+"BLFS","Bathroom"+number+"Bathtub",dbCursor))


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
    #   SINK
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   TOILET
    #-------------------------------------------------------------
    
    #-------------------------------------------------------------
    #   SHOWER
    #-------------------------------------------------------------
    
    #-------------------------------------------------------------
    #   BATHTUB
    #-------------------------------------------------------------

    

def main ():
    bathroom2 = bathroom("Bathroom2", "2", dbCursor,1,0,0)
    bathroom3 = bathroom("Bathroom3", "3", dbCursor,0,1,0)
    bathroom4 = bathroom("Bathroom4", "4", dbCursor,1,0,1)
