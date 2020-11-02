#laundryRoom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class laundryRoom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("laundryRoom Lights",dbCursor)
        self.lights.actuators.append(actuator("laundryRoom Light Actuator","laundryRoom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("LRLBS","laundryRoom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("LRLMS","laundryRoom Lights", dbCursor))

        #-------------------------------------------------------------
        #   door 
        #-------------------------------------------------------------

        self.door = []
        self.door.append(device("LRinteriordoor",dbCursor))
        self.door[0].actuators.append(actuator("laundryRoom Interior Door Actuator", "LRinteriodoor",dbCursor))
        self.door[0].sensors.append(openCloseSensors("LRIDOCS","LRinteriordoor",dbCursor))
        self.door.append(device("LRgaragedoor",dbCursor))
        self.door[1].actuators.append(actuator("laundryRoom Garage Door Actuator", "LRgaragedoor",dbCursor))
        self.door[1].sensors.append(openCloseSensors("LRGDOCS","LRgaragedoor",dbCursor))

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
        self.aircon = device("laundryRoom AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("LRACTS","laundryRoom AirCon",dbCursor))
        self.aircon.actuators.append(actuator("laundryRoom AirCon Actuator","laundryRoom AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("laundryRoom Heat",dbCursor)
        self.heat.actuators.append(actuator("laundryRoom Heat Actuator","laundryRoom Heat",dbCursor))
        self.heat.sensors.append(tempSensor("LRHTS","laundryRoom Heat",dbCursor))
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
        self.dryer.sensors.append(openCloseSensors("DMS","Dryer", dbCursor))

        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokeDetector=device("laundryRoom Smoke Detector",dbCursor)
        self.smokeDetector.actuators.append(actuator("laundryRoom Smoke Detector Actuator","laundryRoom Smoke Detector", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("KSDOCS", "laundryRoom Smoke Detector",dbCursor))
        

    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------
    
    def turnOnLights(self):
        """Turns on the lights."""
        self.lights.actuators[0].turnOn()
    
    def turnOffLights(self):
        """Turns off the lights."""
        self.lights.actuators[0].turnOff()
    
    def getLightsState(self):
        """Returns the light's state (on/off)."""
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,bright):
        """Sets the brightness of the lights.

        Keyword Arguments:
        bright        -- the brigthness of the lights as a percent of its maximum brightness.

        """        
        self.lights.sensors[0].setBrightPct(bright)

    def getLightBrightness(self):
        """Returns the light's brightness."""
        return self.lights.sensors[0].getBrightPct()

    def setLightsMotion(self, value):
        """Sets the light's motion sensor value for motion.

        Keyword Arguments:
        value       -- motion value where 1 is motion and 0 is no motion.

        """
        self.lights.sensors[1].updateIsMotion(value)

    def getLightsMotion(self):
        """Returns the light's motion sensor value."""
        return self.lights.sensors[1].getMotion()
    
    #-------------------------------------------------------------
    #  DOORS
    #-------------------------------------------------------------

    def openDoor(self,doorNum):
        self.door[doorNum].actuators[0].turnOn()
        self.door[doorNum].sensors[0].updateOpen()

    def closeDoor(self,doorNum):
        self.door[doorNum].actuators[0].turnOff()
        self.door[doorNum].sensors[0].updateClosed()

    def getdoortate(self,doorNum):
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

    def turnOnAC(self,frame):
        """Turns on the AC."""
        self.aircon.actuators[0].turnOn()
        frame.aCStateDisplayLabel.config(text="On")
        frame.update()

    def turnOffAC(self,frame):
        """Turns off the AC."""
        self.aircon.actuators[0].turnOff()
        frame.aCStateDisplayLabel.config(text="Off")
        frame.update()

    def getACState(self):
        """Returns the AC's state (on/off)."""
        return self.aircon.actuators[0].getState()

    def setACTemp(self,temp):
        """Sets the AC's temp.

        Keyword Arguments:
        temp        -- the temperature in degrees F.

        """
        self.aircon.sensors[0].setTemp(temp)

    def getACTemp(self):
        """Returns the AC's temp."""
        return self.aircon.sensors[0].getTemp()

    def updateACTemp(self):
        """Update the room's temp when AC is on."""
        currTemp = self.getTemp()
        newTemp = currTemp + self.ACDELTAT
        self.setACTemp(newTemp)
        self.setHeatTemp(newTemp)

    #HEAT
    def turnOnHeat(self,frame):
        """Turns on the heat."""
        self.heat.actuators[0].turnOn()
        frame.heatStateDisplayLabel.config(text="On")
        frame.update()

    def turnOffHeat(self,frame):
        """Turns off the heat."""
        self.heat.actuators[0].turnOff()
        frame.heatStateDisplayLabel.config(text="Off")
        frame.update()

    def getHeatState(self):
        """Returns the heat's state (on/off)."""
        return self.heat.actuators[0].getState()

    def setHeatTemp(self, temp):
        """Sets the heat's temp.

        Keyword Arguments:
        temp        -- the temperature in degrees F.

        """
        self.heat.sensors[0].setTemp(temp)

    def getHeatTemp(self):
        """Returns the heat's temp."""
        return self.heat.sensors[0].getTemp()

    def updateHeatTemp(self):
        """Updates the room's temp when the heat is on."""
        currTemp = self.getTemp()
        newTemp = currTemp + self.HEATDELTAT
        self.setACTemp(newTemp)
        self.setHeatTemp(newTemp)

    #Shared
    def getTemp(self):
        """Checks the temp of the room by comparing both AC and Heat systems temp sensors. Returns the temp if they are the same errors other wise."""
        if self.getACTemp() == self.getHeatTemp():
            return self.getACTemp()
        else:
            print("error temp sensors missmatched (should never be here)")

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------
    
    def turnOnSink(self):
        """Turns on the laundryRoom sink."""
        self.sink.actuators[0].turnOn()

    def turnOffSink(self):
        """Turns off the laundryRoom sink."""
        self.sink.actuators[0].turnOff()

    def getSinkState(self):
        """Returns the laundryRoom sink's state (on/off)."""
        return self.sink.actuators[0].getState()

    def setSinkFlow(self, flowRate):
        """Sets the flow rate of the laundryRoom sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.sink.sensors[0].setFlowRatePct(flowRate)

    def getSinkFlow(self):
        """Returns the laundryRoom sink's flow rate."""
        return self.sink.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   WASHING MACHINE need cycle notification
    #-------------------------------------------------------------

    def turnOnWashingMachine(self):
        self.washingmachine.actuators[0].turnOn()

    def turnOffWashingMachine(self):
        self.washingmachine.actuators[0].turnOff()


    #-------------------------------------------------------------
    #   DRYER need cycle notification moisture sensor?
    #-------------------------------------------------------------

    def turnOnDryer(self):
        self.dryer.actuators[0].turnOn()

    def turnOffDryer(self):
        self.dryer.actuators[0].turnOff()


    #-------------------------------------------------------------
    #   SMOKE ALARM
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


    test=laundryRoom("laundryRoom",cursor)

    test.openDoor(0)
    test.setSmokeState(1)
    print(test.getTemp())

    db.commit()
    db.close()
main()  