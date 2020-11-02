#diningRoom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class diningRoom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("diningRoom Lights",dbCursor)
        self.lights.actuators.append(actuator("diningRoom Light Actuator","diningRoom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("DRLBS","diningRoom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("DRLMS","diningRoom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        #   NO DOORS

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("diningRoom window",dbCursor))
        self.windows[0].actuators.append(actuator("diningRoom window Actuator", "diningRoom window",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("DRWOCS","diningRoom window",dbCursor))


        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("diningRoom AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("DRACTS","diningRoom AirCon",dbCursor))
        self.aircon.actuators.append(actuator("diningRoom AirCon Actuator","diningRoom AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("diningRoom Heat",dbCursor)
        self.heat.actuators.append(actuator("diningRoom Heat Actuator","diningRoom Heat",dbCursor))
        self.heat.sensors.append(tempSensor("DRHTS","diningRoom Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokeDetector=device("diningRoom Smoke Detector",dbCursor)
        self.smokeDetector.actuators.append(actuator("diningRoom Smoke Detector Actuator","diningRoom Smoke Detector", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("DRSDOCS", "diningRoom Smoke Detector",dbCursor))

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("WetBar Sink", dbCursor)
        self.sink.actuators.append(actuator("WetBar Sink Actuator","WetBar Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("WBSLFS","WetBar Sink",dbCursor))


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

    # NO DOORS

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

def main():
    # Open database connection
    db = pymysql.connect("localhost","root","Audrey1!seed","digitalhome" )
    # db = pymysql.connect("localhost","jp","Database","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM TempSensors")
    cursor.execute("DELETE FROM OpenCloseSensors")
    cursor.execute("DELETE FROM MotionSensors")
    cursor.execute("DELETE FROM LiquidFlowSensors")
    cursor.execute("DELETE FROM BrightnessSensor")
    cursor.execute("DELETE FROM Actuators")
    cursor.execute("DELETE FROM Devices")


    test=diningRoom("diningRoom",cursor)

   
    test.setSmokeState(1)
    print(test.getTemp())

    db.commit()
    db.close()
main() 