#breakfastNook.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class breakfastNook:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("breakfastNook Lights",dbCursor)
        self.lights.actuators.append(actuator("breakfastNook Light Actuator","breakfastNook Lights",dbCursor))
        self.lights.sensors.append(brightSensor("BNLBS","breakfastNook Lights", dbCursor))
        self.lights.sensors.append(motionSensor("BNLMS","breakfastNook Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        #   NO DOORS

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("BNWindow1",dbCursor))
        self.windows[0].actuators.append(actuator("breakfastNook Window 1 Actuator", "BNWindow1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("BNW1OCS","BNWindow1",dbCursor))
        self.windows.append(device("BNWindow2",dbCursor))
        self.windows[1].actuators.append(actuator("breakfastNook Window 2 Actuator", "BNWindow2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("BNW2OCS","BNWindow2",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("breakfastNook AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("BNACTS","breakfastNook AirCon",dbCursor))
        self.aircon.actuators.append(actuator("breakfastNook AirCon Actuator","breakfastNook AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("breakfastNook Heat",dbCursor)
        self.heat.actuators.append(actuator("breakfastNook Heat Actuator","breakfastNook Heat",dbCursor))
        self.heat.sensors.append(tempSensor("BNHTS","breakfastNook Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokeDetector=device("breakfastNook Smoke Detector",dbCursor)
        self.smokeDetector.actuators.append(actuator("breakfastNook Smoke Detector Actuator","breakfastNook Smoke Detector", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("BNSDOCS", "breakfastNook Smoke Detector",dbCursor))
        


    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    def turnOnLights(self,frame,db):
        self.lights.actuators[0].turnOn()
        frame.breakfastNookLightsStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()
    
    def turnOffLights(self,frame,db):
        self.lights.actuators[0].turnOff()
        self.setLightBrightness(frame, 0, db)
        frame.breakfastNookLightsStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()
    
    def getLightsState(self):
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,frame,bright,db):
        self.lights.sensors[0].setBrightPct(bright)
        self.turnOnLights(frame,db)
        frame.breakfastNookLightsBrightValueDisplayLabel.config(text=str(bright)+"%")
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

    # NO DOORS

    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    def openWindow(self,winNum,frame,db):
        self.windows[winNum].actuators[0].turnOn()
        self.windows[winNum].sensors[0].updateOpen()
        frame.windowStateDisplayLabel[winNum].config(text="Open")
        frame.update()
        db.commit()

    def closeWindow(self,winNum,frame,db):
        self.windows[winNum].actuators[0].turnOff()
        self.windows[winNum].sensors[0].updateClosed()
        frame.windowStateDisplayLabel[winNum].config(text="Closed")
        frame.update()
        db.commit()

    def getWindowState(self,winNum):
        return self.windows[winNum].actuators[0].getState()

    def getWindowOpenCloseState(self, winNum):
        return self.windows[winNum].sensors[0].getState()

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #AC
    def turnOnAC(self,frame,db):
        self.aircon.actuators[0].turnOn()
        frame.aCStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()


    def turnOffAC(self,frame,db):
        self.aircon.actuators[0].turnOff()
        frame.aCStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

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
    def turnOnHeat(self,frame,db):
        self.heat.actuators[0].turnOn()
        frame.heatStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffHeat(self,frame,db):
        self.heat.actuators[0].turnOff()
        frame.heatStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

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
    #   SMOKE Detector
    #-------------------------------------------------------------

    def turnOnSmokeDetector(self):
        """Turns on the smoke detector."""
        self.smokeDetector.actuators[0].turnOn()

    def turnOffSmokeDetector(self):
        """Turns off the smoke detector."""
        self.smokeDetector.actuators[0].turnOff()

    def getSmokeDetectorState(self):
        """Returns the smoke detector's state (on/off)."""
        return self.smokeDetector.actuators[0].getState()

    def setSmokeState(self, isSmoke):
        """Sets the smoke detector's is smoke state.

        Keyword arguments:
        isSmoke     -- the value representing the presence of smoke. 1 if there is smoke 0 if there is not smoke.

        """
        if isSmoke == 1:
            self.smokeDetector.sensors[0].updateOpen()
        else:
            self.smokeDetector.sensors[0].updateClosed()
    
    def getSmokeState(self):
        """Returns the smoke detector's smoke state (1=smoke/0=nosmoke).
        """
        return self.smokeDetector.sensors[0].getState()


# def main():
#     # Open database connection
#     db = pymysql.connect("localhost","root","Audrey1!seed","digitalhome" )

#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
    
#     cursor.execute("DELETE FROM TempSensors")
#     cursor.execute("DELETE FROM OpenCloseSensors")
#     cursor.execute("DELETE FROM MotionSensors")
#     cursor.execute("DELETE FROM LiquidFlowSensors")
#     cursor.execute("DELETE FROM BrightnessSensor")
#     cursor.execute("DELETE FROM Actuators")
#     cursor.execute("DELETE FROM Devices")


#     bN = breakfastNook("breakfastNook", cursor)
# #    Testing all elements of the breakfastNook

#     print("------------------------------------------")
#     print("TESTING LIGHTS")
#     print(bN.getLightsState())
#     bN.turnOnLights()
#     print(bN.getLightsState())
#     bN.turnOffLights()
#     print(bN.getLightsState())
#     print(bN.getLightBrightness())
#     bN.setLightBrightness(.129837)
#     print(bN.getLightBrightness())
#     print(bN.getLightsMotion())
#     bN.setLightsMotion(1)
#     print(bN.getLightsMotion())
#     print("------------------------------------------")
#     print("TESTING AC/HEAT")
#     print(bN.getACState())
#     bN.turnOnAC()
#     print(bN.getACState())
#     bN.turnOffAC()
#     print(bN.getACState())
#     print(bN.getACTemp())
#     bN.setACTemp(1290470)
#     print(bN.getACTemp())
#     print(bN.getHeatState())
#     bN.turnOnHeat()
#     print(bN.getHeatState())
#     bN.turnOffHeat()
#     print(bN.getHeatState())
#     print(bN.getHeatTemp())
#     bN.setHeatTemp(9182791823719283)
#     print(bN.getHeatTemp())
#     print("------------------------------------------")
#     print("TESTING SMOKE DETECTOR")
#     print(bN.getSmokeDetectorState())
#     bN.turnOnSmokeDetector()
#     print(bN.getSmokeDetectorState())
#     bN.turnOffSmokeDetector()
#     print(bN.getSmokeDetectorState())
#     print(bN.getSmokeState())
#     bN.setSmokeState(1)
#     print(bN.getSmokeState())


#     db.commit()
#     db.close()
# main()  