#laundry_room.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class laundry_room:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Laundry Room Lights",dbCursor)
        self.lights.actuators.append(actuator("Laundry Room Light Actuator","Laundry Room Lights",dbCursor))
        self.lights.sensors.append(brightSensor("LRLBS","Laundry Room Lights", dbCursor))
        self.lights.sensors.append(motionSensor("LRLMS","Laundry Room Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("LRinteriordoor",dbCursor))
        self.doors[0].actuators.append(actuator("Laundry Room Interior Door Actuator", "LRinteriodoor",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("LRIDOCS","LRinteriordoor",dbCursor))
        self.doors.append(device("LRgaragedoor",dbCursor))
        self.doors[1].actuators.append(actuator("Laundry Room Garage Door Actuator", "LRgaragedoor",dbCursor))
        self.doors[1].sensors.append(openCloseSensors("LRGDOCS","LRgaragedoor",dbCursor))

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
        self.aircon = device("Laundry_Room AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("LRACTS","Laundry_Room AirCon",dbCursor))
        self.aircon.actuators.append(actuator("Laundry_Room AirCon Actuator","Laundry_Room AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("Laundry_Room Heat",dbCursor)
        self.heat.actuators.append(actuator("Laundry_Room Heat Actuator","Laundry_Room Heat",dbCursor))
        self.heat.sensors.append(tempSensor("LRHTS","Laundry_Room Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("Sink", dbCursor)
        self.sink.actuators.append(actuator("Sink Actuator","Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("SLFS","Sink",dbCursor))

        #-------------------------------------------------------------
        #   WASHING MACHINE
        #-------------------------------------------------------------

        self.washingmachine = device("Washing Machine",dbCursor)
        self.washingmachine.actuators.append(actuator("Washing Machine Actuator", "Washing Machine", dbCursor))
        self.washingmachine.sensors.append(liquidFlowSensor("WMLFS","Washing Machine", dbCursor))

        #-------------------------------------------------------------
        #   DRYER
        #-------------------------------------------------------------

        self.dryer = device("Dryer",dbCursor)
        self.dryer.actuators.append(actuator("Dryer Actuator", "Dryer", dbCursor))
        self.dryer.sensors.append(MoistureSensor("DMS","Dryer", dbCursor))

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokedetector = device("Smoke Detector", dbCursor)
        self.smokedetector.sensor.append(openCloseSensors("LRSS","Smoke Detector", dbCursor))


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

    #   NO WINDOWS

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
    #   WASHING MACHINE
    #-------------------------------------------------------------

    def turnOnWashingMachine(self):
        self.washingmachine.actuators[0].turnOn()

    def turnOffWashingMachine(self):
        self.washingmachine.actuators.[0].turnOff()

    def getWashingMachineState(self):
        return self.washingmachine.actuators[0].getState()

    def setWashingMachineFlow(self, flowRate):
        self.washingmachine.sensors[0].setFlowRatePct(flowRate)

    def getWashingMachineFlow(self):
        return self.washingmachine.sensors[0].getFlowRatePct()


    #-------------------------------------------------------------
    #   DRYER
    #-------------------------------------------------------------

    def turnOnDryer(self):
        self.Dryer.actuators[0].turnOn()

    def turnOffDryer(self):
        self.Dryer.actuators[0].turnOff()
    
    def getDryerState(self):
        return self.dryer.actuators[0].getState()

    def setDryerTemp(self, temp):
        self.dryer.sensors[0].setTemp(temp)

    def getDryerTemp(self):
        self.dryer.sensors[0].getTemp()

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


    test=Laundry_Room("Laundry_Room",cursor)

    test.openDoor(0)
    test.setSmokeState(1)
    print(test.getTemp())

    db.commit()
    db.close()
main()  

  