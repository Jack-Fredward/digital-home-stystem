#Michelle_Bedroom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class Michelle_Bedroom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Michelle_Bedroom Lights",dbCursor)
        self.lights.actuators.append(actuator("Michelle_Bedroom Light Actuator","Michelle_Bedroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("MBLBS","Michelle_Bedroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("MBLMS","Michelle_Bedroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("MBinteriordoor",dbCursor))
        self.doors[0].actuators.append(actuator("Michelle_Bedroom Interior Door Actuator", "MBinteriodoor",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("MBIDOCS","MBinteriordoor",dbCursor))
        
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------
        self.windows = device("Michelle_Bedroom window",dbCursor)
        self.windows.append(device("Michelle_Bedroom window",dbCursor))
        self.windows.actuators.append(actuator("Michelle_Bedroom window Actuator", "Michelle_Bedroom window",dbCursor))
        self.windows.sensors.append(openCloseSensors("MBWOCS","Michelle_Bedroom window",dbCursor))
      

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("MBATS","Air",dbCursor))
        self.air.actuators.append(actuator("Michelle_Bedroom Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        self.cameras = device("Michelle_Bedroom Camera",dbCursor)
        self.cameras.append(device("Michelle_Bedroom Camera",dbCursor))
        self.cameras.actuators.append(actuator("Michelle_Bedroom Camera Actuator","Michelle_Bedroom Camera",dbCursor))
        self.cameras.sensors.append(motionSensor("MBCMS","Michelle_Bedroom Camera",dbCursor))

        
        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Smoke Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("MBSS","Smoke Alarm", dbCursor))

        #-------------------------------------------------------------
        #   SMOKE detector 
        #-------------------------------------------------------------
        self.smokealarm = device("Michelle_Bedroom Detector", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("MBSS","Michelle_Bedroom Detector", dbCursor))



    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------
def turnOnLights(self):
    #turns on the lights
        self.lights.actuators[0].turnOn()
    
def turnOffLights(self):
    #turns off the lights
        self.lights.actuators[0].turnOff()
    
def getLightsState(self): 
            #Returns the light's state (on/off)
            return self.lights.actuators[0].getState()

def setLightBrightness(self,bright):
             #set the brightness of the lights
                self.lights.sensors[0].setBrightPct(bright)

def getLightBrightness(self):
        #returns the light's brightness
            return self.lights.sensors[0].getBrightPct()

def setLightsMotion(self, value):
        #sets the lights motion sensor vaule for motion 
        self.lights.sensors[1].updateIsMotion(value)

def getLightsMotion(self):
        #returns the light's motion sensor value 
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
        #turns on the AC
        self.aircon.actuators[0].turnOn()

def turnOffAC(self):
        #turns off the AC 
        self.aircon.actuators[0].turnOff()

def getACState(self):
        #returns the AC's state temp 
        return self.aircon.actuators[0].getState()

def setACTemp(self,temp):
        #sets the AC's temp
        self.aircon.sensors[0].setTemp(temp)

def getACTemp(self):
    #returns the AC's temp 
        return self.aircon.sensors[0].getTemp()

def updateACTemp(self):
        #update the room's temp when AC  is on 
        currTemp = self.getTemp()
        newTemp = currTemp + self.ACDELTAT
        self.setACTemp(newTemp)
        self.setHeatTemp(newTemp)

    #HEAT
def turnOnHeat(self):
        #turns on heat 
        self.heat.actuators[0].turnOn()

def turnOffHeat(self):
        #turns off heat
        self.heat.actuators[0].turnOff()

def getHeatState(self):
        #returns the heat's state  on/off
        return self.heat.actuators[0].getState()

def setHeatTemp(self, temp):
        #sets the heat's temp
        self.heat.sensors[0].setTemp(temp)

def getHeatTemp(self):
        #returns the heat's temp
        return self.heat.sensors[0].getTemp()

def updateHeatTemp(self):
        #update the room's temp when the heat is on 
        currTemp = self.getTemp()
        newTemp = currTemp + self.HEATDELTAT
        self.setACTemp(newTemp)
        self.setHeatTemp(newTemp)

    #Shared
def getTemp(self):
        #checks the temp of the room by comparing both AC and heat systems temp sensors.returns the temp if they are the error other wise
        if self.getACTemp() == self.getHeatTemp():
            return self.getACTemp()
        else:
            print("error temp sensors missmatched (should never be here)")

    #-------------------------------------------------------------
    #   CAMERAS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------
    
    #-------------------------------------------------------------
    #   somke detector
    #-------------------------------------------------------------
def turnOnSmokeDetector(self):
    #turns on the smoke deterctor 
        self.smokeDetector.actuators[0].turnOn()

def turnOffSmokeDetector(self):
        #turns off the smoke detector
        self.smokeDetector.actuators[0].turnOff()

def getSmokeDetectorState(self):
        #returns the smoke detector's state on/off
        return self.smokeDetector.actuators[0].getState()

def setSmokeState(self, isSmoke):
        #sets the smoke detector's is smoke state 
        if isSmoke == 1:
            self.smokeDetector.sensors[0].updateOpen()
        else:
            self.smokeDetector.sensors[0].updateClosed()
    

def getSmokeState(self):
        #returns the smoke detector's smoke state (1=smoke/0=nosmoke)
        return self.smokeDetector.sensors[0].getState()

    

    #-------------------------------------------------------------
    #   DRYER need cycle notification moisture sensor?
    #-------------------------------------------------------------

   
    #-------------------------------------------------------------
    #   SMOKE ALARM
    #-------------------------------------------------------------

  
