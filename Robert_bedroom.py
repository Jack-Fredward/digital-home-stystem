#Robert's_bedroom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbaCursor = dbCursor
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

        self.lights = device("Robert_bedroom Lights",dbCursor)
        self.lights.actuators.append(actuator("Robert_bedroom Light Actuator","Robert_bedroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("RBLBS","Robert_bedroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("RBLMS","Robert_bedroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("RBinteriordoor",dbCursor))
        self.doors[0].actuators.append(actuator("Robert_bedroom Interior Door Actuator", "RBinteriodoor",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("RBIDOCS","RBinteriordoor",dbCursor))
        
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------
        
        self.windows = device("Robert_bedroom window",dbCursor)
        self.windows.append(device("Robert_bedroom window",dbCursor))
        self.windows.actuators.append(actuator("Robert_bedroom window Actuator", "Robert_bedroom window",dbCursor))
        self.windows.sensors.append(openCloseSensors("RBWOCS","Robert_bedroom window",dbCursor))
      

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("RBATS","Air",dbCursor))
        self.air.actuators.append(actuator("Robert_bedroom Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------
        self.cameras = device("Robert_bedroom",dbCursor)
        self.cameras.append(device("Robert_bedroom",dbCursor))
        self.cameras.actuators.append(actuator("Robert_bedroom Camera Actuator","Robert_bedroom",dbCursor))
        self.cameras.sensors.append(motionSensor("RBCMS","Robert_bedroom",dbCursor))

        
        
        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Smoke Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("RBSS","Smoke Alarm", dbCursor))


    #-------------------------------------------------------------
    #-------------------------------------------------------------
    #   smoke detector
    #-------------------------------------------------------------
        self.smokealarm = device("Robert_bedroom Detector", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("RBSS","Robert_bedroom Detector", dbCursor))


    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   CAMERAS
    #-------------------------------------------------------------



    
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

  


     