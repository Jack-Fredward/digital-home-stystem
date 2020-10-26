#living_room.py

import pymysql
from device import *
import datetime

class Living_Room:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Living_Room Lights",dbCursor)
        self.lights.actuators.append(actuator("Living_Room Light Actuator","Living_Room Lights",dbCursor))
        self.lights.sensors.append(brightSensor("LRLBS","Living_Room Lights", dbCursor))
        self.lights.sensors.append(motionSensor("LRLMS","Living_Room Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = device("Living_Room door", dbCursor)
        self.doors.append(device("Living_Room door",dbCursor))
        self.doors.actuators.append(actuator("Living_Room Door Actuator", "Living_Room door",dbCursor))
        self.doors.sensors.append(openCloseSensors("LRDOCS","Living_Room door",dbCursor))
       

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        # NO WINDOWS

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("LRATS","Air",dbCursor))
        self.air.actuators.append(actuator("Living_Room Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokealarm = device("Living_Room Detector", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("LRSS","Living_Room Detector", dbCursor))

        #-------------------------------------------------------------
        #   FIREPLACE
        #-------------------------------------------------------------

        self.fireplace = device("Fireplace", dbCursor)
        self.fireplace.actuators.append(actuator("Fireplace Actuator", "Fireplace", dbCursor))
        self.fireplace.sensors.append(tempSensor("FTS","Fireplace",dbCursor))

        #-------------------------------------------------------------
        #   TELEVISION
        #-------------------------------------------------------------

        self.television = device("Television",dbCursor)
        self.television.actuators.append(actuator("Television Actuator", "Television",dbCursor))

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

    # NO WINDOWS

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
    #   SMOKE DETECTOR
    #-------------------------------------------------------------

    def turnOnSmokeDetector(self):
        self.smokeDetector.actuators[0].turnOn()

    def turnOffSmokeDetector(self):
        self.smokeDetector.actuators[0].turnOff()

    def getSmokeDetectorState(self):
        return self.smokeDetector.actuators[0].getState()

    def setSmokeState(self, isSmoke):
        if isSmoke == 1:
            self.smokeDetector.sensors[0].updateOpen()
        else:
            self.smokeDetector.sensors[0].updateClosed()
    
    def getSmokeState(self):
        return self.smokeDetector.sensors[0].getState()

    #-------------------------------------------------------------
    #   FIREPLACE
    #-------------------------------------------------------------

    def turnOnFireplace(self):
        self.fireplace.actuators[0].turnOn()

    def turnOffFireplace(self):
        self.fireplace.actuators[0].turnOff()

    def getFireplaceState(self):
        return self.fireplace.actuators[0].getState()

    def setFireplaceTemp(self, temp):
        self.fireplace.sensors[0].setTemp(temp)

    def getFireplaceTemp(self):
        self.fireplace.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   TELEVISION
    #-------------------------------------------------------------

    def turnOnTelevision(self):
        self.television.actuators[0].turnOn()

    def turnOffTelevision(self):
        self.television.actuators[0].turnOff()

    def getTelevisionState(self):
        return self.television.actuators[0].getState()