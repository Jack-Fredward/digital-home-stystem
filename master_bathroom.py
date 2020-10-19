#master_bathroom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class master_bathroom:
    def __init__(self, name, number, dbCursor, has_shower, has_bathtub, has_extDoor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Master_Bathroom Lights",dbCursor)
        self.lights.actuators.append(actuator("Master_Bathroom Light Actuator","Master_Bathroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("MBLBS","Master_Bathroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("MBLMS","Master_Bathroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("Master_Bathroom door",dbCursor))
        self.doors[0].actuators.append(actuator("Master_Bathroom Door Actuator", "Master_Bathroom door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("MBDOCS","Master_Bathroom door",dbCursor))
        self.doors.append(device("Master_Bathroom Closet door",dbCursor))
        self.doors[1].actuators.append(actuator("Master_Bathroom Closet Door Actuator", "Master_Bathroom Closet door",dbCursor))
        self.doors[1].sensors.append(openCloseSensors("MBCDOCS","Master_Bathroom Closet door",dbCursor))
        self.doors.append(device("Master_Bathroom His door",dbCursor))
        self.doors[2].actuators.append(actuator("Master_Bathroom His Door Actuator", "Master_Bathroom His door",dbCursor))
        self.doors[2].sensors.append(openCloseSensors("MBHDOCS","Master_Bathroom His door",dbCursor))
        self.doors.append(device("Master_Bathroom Her door",dbCursor))
        self.doors[3].actuators.append(actuator("Master_Bathroom Her Door Actuator", "Master_Bathroom Her door",dbCursor))
        self.doors[3].sensors.append(openCloseSensors("MBHERDOCS","Master_Bathroom Her door",dbCursor))
      
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = device("Master_Bathroom window",dbCursor)
        self.windows.append(device("Master_Bathroom window",dbCursor))
        self.windows.actuators.append(actuator("Master_Bathroom window Actuator", "Master_Bathroom window",dbCursor))
        self.windows.sensors.append(openCloseSensors("MBWOCS","Master_Bathroom window",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("MBATS","Air",dbCursor))
        self.air.actuators.append(actuator("Master_Bathroom Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = []
        self.sink.append(device("Master_Bathroom His sink",dbCursor))
        self.sink[0].actuators.append(actuator("Master_Bathroom His Sink Actuator","Master_Bathroom His Sink",dbCursor))
        self.sink[0].sensors.append(liquidFlowSensor("MBHSLFS","Master_Bathroom His Sink",dbCursor))
        self.sink.append(device("Master_Bathroom Her sink",dbCursor))
        self.sink[1].actuators.append(actuator("Master_Bathroom Her Sink Actuator","Master_Bathroom Her Sink",dbCursor))
        self.sink[1].sensors.append(liquidFlowSensor("MBHERSLFS","Master_Bathroom Her Sink",dbCursor))
       
        #-------------------------------------------------------------
        #   TOILET
        #-------------------------------------------------------------
 
        self.toilet = []
        self.toilet.append(device("Master_Bathroom His toilet",dbCursor))
        self.toilet[0].actuators.append(actuator("Master_Bathroom His toilet Actuator","Master_Bathroom His toilet",dbCursor))
        self.toilet[0].sensors.append(liquidFlowSensor("MBHTLFS","Master_Bathroom His toilet",dbCursor))
        self.toilet.append(device("Master_Bathroom Her toilet",dbCursor))
        self.toilet[1].actuators.append(actuator("Master_Bathroom Her toilet Actuator","Master_Bathroom Her toilet",dbCursor))
        self.toilet[1].sensors.append(liquidFlowSensor("MBHERTLFS","Master_Bathroom Her toilet",dbCursor))

        #-------------------------------------------------------------
        #   SHOWER
        #-------------------------------------------------------------


        self.shower = device("Master_Bathroom shower",dbCursor)
        self.shower = device("Master_Bathroom Shower", dbCursor)
        self.shower.actuators.append(actuator("Master_Bathroom Shower Actuator","Master_Bathroom Shower",dbCursor))
        self.shower.sensors.append(liquidFlowSensor("MBSHLFS","Master_Bathroom Shower",dbCursor))

        #-------------------------------------------------------------
        #   BATHTUB
        #-------------------------------------------------------------
        
   
        self.bathtub = device("Master_Bathroom bathtub",dbCursor)
        self.bathtub = device("Master_Bathroom bathtub", dbCursor)
        self.bathtub.actuators.append(actuator("Master_Bathroom Bathtub Actuator","Master_Bathroom Bathtub",dbCursor))
        self.bathtub.sensors.append(liquidFlowSensor("MBBLFS","Master_Bathroom Bathtub",dbCursor))


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

    

