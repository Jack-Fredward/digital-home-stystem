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

        self.windows = []
        self.windows.append(device("MBWindow1",dbCursor))
        self.windows[0].actuators.append(actuator("Master_Bathroom Window 1 Actuator", "MBwindow1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("MBW1OCS","MBWindow1",dbCursor))
        self.windows.append(device("MBWindow2",dbCursor))
        self.windows[1].actuators.append(actuator("Master_Bathroom Window 2 Actuator", "MBwindow2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("MBW2OCS","MBWindow2",dbCursor))
        self.windows.append(device("MBWindow3",dbCursor))
        self.windows[2].actuators.append(actuator("Master_Bathroom Window 3 Actuator", "MBwindow3",dbCursor))
        self.windows[2].sensors.append(openCloseSensors("MBW3OCS","MBWindow3",dbCursor))
        self.windows.append(device("MBWindow4",dbCursor))
        self.windows[3].actuators.append(actuator("Master_Bathroom Window 4 Actuator", "MBwindow4",dbCursor))
        self.windows[3].sensors.append(openCloseSensors("MBW4OCS","MBWindow4",dbCursor))
        self.windows.append(device("MBWindow4",dbCursor))
        self.windows[4].actuators.append(actuator("Master_Bathroom Window 5 Actuator", "MBwindow5",dbCursor))
        self.windows[4].sensors.append(openCloseSensors("MBW5OCS","MBWindow5",dbCursor))

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

    def turnOnLights(self):
        self.lights.actuators[0].turnOn()
    
    def turnOffLights(self):
        self.lights.actuators[0].turnOff()
    
    def getLightsState(self):
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,bright):
        self.lights.sensors[0].setBrightPct(bright)

    def getLightBrightness(self):
        return self.lights.sensors[0].getBrightPct()

    def setLightsMotion(self, value):
        self.lights.sensors[1].updateIsMotion(value)

    def getLightsMotion(self):
        return self.lights.sensors[1].getMotion()

    #-------------------------------------------------------------
    #   DOORS
    #-------------------------------------------------------------

    def openDoor(self,doorNum):
        self.door[doorNum].actuators[0].turnOn()
        self.door[doorNum].sensors[0].updateOpen()

    def closeDoor(self,doorNum):
        self.door[doorNum].actuators[0].turnOff()
        self.door[doorNum].sensors[0].updateClosed()

    def getDoorState(self,doorNum):
        return self.door[doorNum].actuators[0].getState()

    def getDoorOpenCloseState(self,doorNum):
        return self.door[doorNum].sensors[0].getState()


    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    def openWindow(self,winNum):
        self.windows[winNum].actuators[0].turnOn()
        self.windows[winNum].sensors[0].updateOpen()

    def closeWindow(self,winNum):
        self.windows[winNum].actuators[0].turnOff()
        self.windows[winNum].sensors[0].updateClosed()

    def getWindowState(self,winNum):
        return self.windows[winNum].actuators[0].getState()

    def getWindowOpenCloseState(self, winNum):
        return self.windows[winNum].sensors[0].getState()

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #AC
    def turnOnAC(self):
        self.aircon.actuators[0].turnOn()

    def turnOffAC(self):
        self.aircon.actuators[0].turnOff()

    def getACState(self):
        return self.aircon.actuators[0].getState()

    def setACTemp(self,temp):
        self.aircon.sensors[0].setTemp(temp)

    def getACTemp(self):
        return self.aircon.sensors[0].getTemp()

    def updateACTemp(self):
        currTemp = self.getTemp()
        newTemp = currTemp + self.ACDELTAT
        self.setACTemp(newTemp)
        self.setHeatTemp(newTemp)

    #HEAT
    def turnOnHeat(self):
        self.heat.actuators[0].turnOn()

    def turnOffHeat(self):
        self.heat.actuators[0].turnOff()

    def getHeatState(self):
        return self.heat.actuators[0].getState()

    def setHeatTemp(self, temp):
        self.heat.sensors[0].setTemp(temp)

    def getHeatTemp(self):
        return self.heat.sensors[0].getTemp()

    def updateHeatTemp(self):
        currTemp = self.getTemp()
        newTemp = currTemp + self.HEATDELTAT
        self.setACTemp(newTemp)
        self.setHeatTemp(newTemp)

    #Shared
    def getTemp(self):
        if self.getACTemp() == self.getHeatTemp():
            return self.getACTemp()
        else:
            print("error temp sensors missmatched (should never be here)")

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------
   
    def turnOnSink(self):
        self.sink.actuators[0].turnOn()

    def turnOffSink(self):
        self.sink.actuators[0].turnOff()

    def getSinkState(self):
        return self.sink.actuators[0].getState()

    def setSinkFlow(self, flowRate):
        self.sink.sensors[0].setFlowRatePct(flowRate)

    def getSinkFlow(self):
        return self.sink.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   TOILET
    #-------------------------------------------------------------
    
    def turnOnToilet(self):
        self.toilet.actuators[0].turnOn()

    def turnOffToilet(self):
        self.toilet.actuators[0].turnOff()

    def getToiletState(self):
        return self.toilet.actuators[0].getState()

    def setToiletFlow(self, flowRate):
        self.toilet.sensors[0].setFlowRatePct(flowRate)

    def getToiletFlow(self):
        return self.toilet.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   SHOWER
    #-------------------------------------------------------------
    
    def turnOnShower(self):
        self.shower.actuators[0].turnOn()

    def turnOffShower(self):
        self.shower.actuators[0].turnOff()

    def getShowerState(self):
        return self.shower.actuators[0].getState()

    def setShowerFlow(self, flowRate):
        self.shower.sensors[0].setFlowRatePct(flowRate)

    def getShowerFlow(self):
        return self.shower.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   BATHTUB
    #-------------------------------------------------------------

    def turnOnBathtub(self):
        self.bathtub.actuators[0].turnOn()

    def turnOffBathtub(self):
        self.bathtub.actuators[0].turnOff()

    def getBathtubState(self):
        return self.bathtub.actuators[0].getState()

    def setBathtubFlow(self, flowRate):
        self.bathtub.sensors[0].setFlowRatePct(flowRate)

    def getBathtubFlow(self):
        return self.bathtub.sensors[0].getFlowRatePct()