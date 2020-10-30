#master_bedroom.py

import pymysql
from device import *
import datetime

class Master_Bedroom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Master_Bedroom Lights",dbCursor)
        self.lights.actuators.append(actuator("Master_Bedroom Light Actuator","Master_Bedroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("MBDLBS","Master_Bedroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("MBDLMS","Master_Bedroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("MBDDoors1",dbCursor))
        self.doors[0].actuators.append(actuator("Master Bedroom Doors 1 Actuator", "MBDDoors1",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("MBDD1OCS","MBDDoors1",dbCursor))
        self.doors.append(device("MBDDoors2",dbCursor))
        self.doors[1].actuators.append(actuator("Master Bedroom Doors 2 Actuator", "MBDDoors2",dbCursor))
        self.doors[1].sensors.append(openCloseSensors("MBDD2OCS","MBDDoors2",dbCursor))
        

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("MBDWindow1",dbCursor))
        self.windows[0].actuators.append(actuator("Master_Bedroom Window 1 Actuator", "MBDwindow1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("MBDW1OCS","MBDWindow1",dbCursor))
        self.windows.append(device("MBDWindow2",dbCursor))
        self.windows[1].actuators.append(actuator("Master_Bedroom Window 2 Actuator", "MBDwindow2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("MBDW2OCS","MBDWindow2",dbCursor))
        self.windows.append(device("MBDWindow3",dbCursor))
        self.windows[2].actuators.append(actuator("Master_Bedroom Window 3 Actuator", "MBDwindow3",dbCursor))
        self.windows[2].sensors.append(openCloseSensors("MBDW3OCS","MBDWindow3",dbCursor))
        self.windows.append(device("MBDWindow4",dbCursor))
        self.windows[3].actuators.append(actuator("Master_Bedroom Window 4 Actuator", "MBDwindow4",dbCursor))
        self.windows[3].sensors.append(openCloseSensors("MBDW4OCS","MBDWindow4",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("Master_Bedroom AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("MBDACTS","Master_Bedroom AirCon",dbCursor))
        self.aircon.actuators.append(actuator("Master_Bedroom AirCon Actuator","Master_Bedroom AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("Master_Bedroom Heat",dbCursor)
        self.heat.actuators.append(actuator("Master_Bedroom Heat Actuator","Master_Bedroom Heat",dbCursor))
        self.heat.sensors.append(tempSensor("MBDHTS","Master_Bedroom Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokeDetector=device("Master_Bedroom Detector", dbCursor)
        self.smokeDetector.actuators.append(actuator("Master_Bedroom Smoke Detector Actuator","Master_Bedroom Smoke Detector", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("MBDSD","Master_Bedroom Detector", dbCursor))

        #-------------------------------------------------------------
        #   BLOOD PRESSURE MONITOR should this have an open close sensor or can we change it to something else?
        #-------------------------------------------------------------

        self.bloodpressuremonitor=device("Blood Pressure Monitor",dbCursor)
        self.bloodpressuremonitor.actuators.append(actuator("Blood Pressure Monitor Actuator","Blood Pressure Monitor", dbCursor))
        self.bloodpressuremonitor.sensors.append(openCloseSensors("BPMOCS", "Blood Pressure Monitor",dbCursor))

        #-------------------------------------------------------------
        #   GLUCOSE MONITOR should this have an open close sensor or can we change it to something else?
        #-------------------------------------------------------------

        self.glucosemonitor=device("Glucose Monitor",dbCursor)
        self.glucosemonitor.actuators.append(actuator("Glucose Monitor Actuator","Glucose Monitor", dbCursor))
        self.glucosemonitor.sensors.append(openCloseSensors("GMOCS", "Glucose Monitor",dbCursor))

        #-------------------------------------------------------------
        #   PULSE OXIMETER should this have an open close sensor or can we change it to something else?
        #-------------------------------------------------------------

        self.pulseoximeter=device("Pulse Oximeter",dbCursor)
        self.pulseoximeter.actuators.append(actuator("Pulse Oximeter Actuator","Pulse Oximeter", dbCursor))
        self.pulseoximeter.sensors.append(openCloseSensors("POOCS", "Pulse Oximeter",dbCursor))

       

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
    #   BLOOD PRESSURE MONITOR
    #-------------------------------------------------------------

    def turnOnbloodpressuremonitor(self):
        self.bloodpressuremonitor.actuators[0].turnOn()

    def turnOffbloodpressuremonitor(self):
        self.bloodpressuremonitor.actuators[0].turnOff()

    def getbloodpressuremonitorState(self):
        return self.bloodpressuremonitor.actuators[0].getState()

    def setbloodpressuremonitorState(self, isHigh):
        if isHigh == 1:
            self.bloodpressuremonitor.sensors[0].updateOpen()
        else:
            self.bloodpressuremonitor.sensors[0].updateClosed()
    


    #-------------------------------------------------------------
    #   GLUCOSE MONITOR
    #-------------------------------------------------------------

    def turnOnglucosemonitor(self):
        self.glucosemonitor.actuators[0].turnOn()

    def turnOffglucosemonitor(self):
        self.glucosemonitor.actuators[0].turnOff()

    def getglucosemonitorState(self):
        return self.glucosemonitor.actuators[0].getState()

    def setglucosemonitorState(self, isHigh):
        if isHigh == 1:
            self.glucosemonitor.sensors[0].updateOpen()
        else:
            self.glucosemonitor.sensors[0].updateClosed()
    


    #-------------------------------------------------------------
    #   PULSE OXIMETER
    #-------------------------------------------------------------
    
    def turnOnpulseoximeter(self):
        self.pulseoximeter.actuators[0].turnOn()

    def turnOffpulseoximeter(self):
        self.pulseoximeter.actuators[0].turnOff()

    def getpulseoximeterState(self):
        return self.pulseoximeter.actuators[0].getState()

    def setpulseoximeterState(self, isLow):
        if isLow == 1:
            self.pulseoximeter.sensors[0].updateOpen()
        else:
            self.pulseoximeter.sensors[0].updateClosed()
    



def main():
    # Open database connection
    db = pymysql.connect("localhost","root","Audrey1!seed","digitalhome" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM TempSensors")
    cursor.execute("DELETE FROM OpenCloseSensors")
    cursor.execute("DELETE FROM MotionSensors")
    cursor.execute("DELETE FROM LiquidFlowSensors")
    cursor.execute("DELETE FROM BrightnessSensor")
    cursor.execute("DELETE FROM Actuators")
    cursor.execute("DELETE FROM Devices")


    test=Master_Bedroom("Master_Bedroom",cursor)

    test.openDoor(0)
    test.setSmokeState(1)
    print(test.getTemp())

    db.commit()
    db.close()
main()