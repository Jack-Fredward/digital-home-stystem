#livingRoom.py

import pymysql
from device import *
import datetime

class livingRoom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("livingRoom Lights",dbCursor)
        self.lights.actuators.append(actuator("livingRoom Light Actuator","livingRoom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("LRLBS","livingRoom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("LRLMS","livingRoom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("livingRoom door",dbCursor))
        self.doors[0].actuators.append(actuator("livingRoom Door Actuator", "livingRoom door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("LRDOCS","livingRoom door",dbCursor))
       

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        # NO WINDOWS

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("livingRoom AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("LRACTS","livingRoom AirCon",dbCursor))
        self.aircon.actuators.append(actuator("livingRoom AirCon Actuator","livingRoom AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("livingRoom Heat",dbCursor)
        self.heat.actuators.append(actuator("livingRoom Heat Actuator","livingRoom Heat",dbCursor))
        self.heat.sensors.append(tempSensor("LRHTS","livingRoom Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokeDetector=device("livingRoom Smoke Detector",dbCursor)
        self.smokeDetector.actuators.append(actuator("livingRoom Smoke Detector Actuator","livingRoom Smoke Detector", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("LRSDOCS", "livingRoom Smoke Detector",dbCursor))

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

    def turnOnLights(self,frame,db):
        self.lights.actuators[0].turnOn()
        frame.studyLightsStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()
    
    def turnOffLights(self,frame,db):
        self.lights.actuators[0].turnOff()
        self.setLightBrightness(frame, 0, db)
        frame.studyLightsStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()
    
    def getLightsState(self):
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,frame,bright,db):
        self.lights.sensors[0].setBrightPct(bright)
        if bright!=0:
            self.turnOnLights(frame,db)
        frame.studyLightsBrightValueDisplayLabel.config(text=str(bright)+"%")
        frame.update()
        db.commit()

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
        self.doors[doorNum].actuators[0].turnOn()
        self.doors[doorNum].sensors[0].updateOpen()

    def closeDoor(self,doorNum):
        self.doors[doorNum].actuators[0].turnOff()
        self.doors[doorNum].sensors[0].updateClosed()

    def getDoorState(self,doorNum):
        return self.doors[doorNum].actuators[0].getState()

    def getDoorOpenCloseState(self,doorNum):
        return self.doors[doorNum].sensors[0].getState()

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


# def main():
#     # Open database connection
#      db = pymysql.connect("localhost","root","Audrey1!seed","digitalhome" )
#     # db = pymysql.connect("localhost","jp","Database","digital_home_database" )

#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
    
#     cursor.execute("DELETE FROM TempSensors")
#     cursor.execute("DELETE FROM OpenCloseSensors")
#     cursor.execute("DELETE FROM MotionSensors")
#     cursor.execute("DELETE FROM LiquidFlowSensors")
#     cursor.execute("DELETE FROM BrightnessSensor")
#     cursor.execute("DELETE FROM Actuators")
#     cursor.execute("DELETE FROM Devices")


#     test=livingRoom("livingRoom",cursor)

#     test.openDoor(0)
#     test.setSmokeState(1)
#     print(test.getTemp())

#     db.commit()
#     db.close()
# main()  