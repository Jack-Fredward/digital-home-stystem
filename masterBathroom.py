#masterBathroom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class masterBathroom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("masterBathroom Lights",dbCursor)
        self.lights.actuators.append(actuator("masterBathroom Light Actuator","masterBathroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("MBLBS","masterBathroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("MBLMS","masterBathroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("masterBathroom door",dbCursor))
        self.doors[0].actuators.append(actuator("masterBathroom Door Actuator", "masterBathroom door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("MBDOCS","masterBathroom door",dbCursor))
        self.doors.append(device("masterBathroom Closet door",dbCursor))
        self.doors[1].actuators.append(actuator("masterBathroom Closet Door Actuator", "masterBathroom Closet door",dbCursor))
        self.doors[1].sensors.append(openCloseSensors("MBCDOCS","masterBathroom Closet door",dbCursor))
        self.doors.append(device("masterBathroom His door",dbCursor))
        self.doors[2].actuators.append(actuator("masterBathroom His Door Actuator", "masterBathroom His door",dbCursor))
        self.doors[2].sensors.append(openCloseSensors("MBHDOCS","masterBathroom His door",dbCursor))
        self.doors.append(device("masterBathroom Her door",dbCursor))
        self.doors[3].actuators.append(actuator("masterBathroom Her Door Actuator", "masterBathroom Her door",dbCursor))
        self.doors[3].sensors.append(openCloseSensors("MBHERDOCS","masterBathroom Her door",dbCursor))
      
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("MBWindow1",dbCursor))
        self.windows[0].actuators.append(actuator("masterBathroom Window 1 Actuator", "MBwindow1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("MBW1OCS","MBWindow1",dbCursor))
        self.windows.append(device("MBWindow2",dbCursor))
        self.windows[1].actuators.append(actuator("masterBathroom Window 2 Actuator", "MBwindow2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("MBW2OCS","MBWindow2",dbCursor))
        self.windows.append(device("MBWindow3",dbCursor))
        self.windows[2].actuators.append(actuator("masterBathroom Window 3 Actuator", "MBwindow3",dbCursor))
        self.windows[2].sensors.append(openCloseSensors("MBW3OCS","MBWindow3",dbCursor))
        self.windows.append(device("MBWindow4",dbCursor))
        self.windows[3].actuators.append(actuator("masterBathroom Window 4 Actuator", "MBwindow4",dbCursor))
        self.windows[3].sensors.append(openCloseSensors("MBW4OCS","MBWindow4",dbCursor))
        self.windows.append(device("MBWindow4",dbCursor))
        self.windows[4].actuators.append(actuator("masterBathroom Window 5 Actuator", "MBwindow5",dbCursor))
        self.windows[4].sensors.append(openCloseSensors("MBW5OCS","MBWindow5",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("masterBathroom AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("MBACTS","masterBathroom AirCon",dbCursor))
        self.aircon.actuators.append(actuator("masterBathroom AirCon Actuator","masterBathroom AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("masterBathroom Heat",dbCursor)
        self.heat.actuators.append(actuator("masterBathroom Heat Actuator","masterBathroom Heat",dbCursor))
        self.heat.sensors.append(tempSensor("MBHTS","masterBathroom Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        #His Sink
        self.sink = device("His Sink", dbCursor)
        self.sink.actuators.append(actuator("Sink Actuator","His Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("HSLFS","His Sink",dbCursor))

        #Her Sink
        self.hersink = device("Her Sink",dbCursor)
        self.hersink.actuators.append(actuator("Her Sink Actuator", "Her Sink", dbCursor))
        self.hersink.sensors.append(liquidFlowSensor("HERSLFS","Her Sink", dbCursor))
       
        #-------------------------------------------------------------
        #   TOILET
        #-------------------------------------------------------------
 
        #His Toilet
        self.toilet = device("His Toilet", dbCursor)
        self.toilet.actuators.append(actuator("His Toilet Actuator","His Toilet",dbCursor))
        self.toilet.sensors.append(liquidFlowSensor("HTLFS","His Toilet",dbCursor))

        #Her Toilet
        self.pantrytoilet = device("Her toilet",dbCursor)
        self.pantrytoilet.actuators.append(actuator("Her toilet Actuator", "Her toilet", dbCursor))
        self.pantrytoilet.sensors.append(liquidFlowSensor("HERTLFS","Her Toilet", dbCursor))

        #-------------------------------------------------------------
        #   SHOWER
        #-------------------------------------------------------------


        self.shower = device("masterBathroom shower",dbCursor)
        self.shower.actuators.append(actuator("masterBathroom Shower Actuator","masterBathroom Shower",dbCursor))
        self.shower.sensors.append(liquidFlowSensor("MBSHLFS","masterBathroom Shower",dbCursor))

        #-------------------------------------------------------------
        #   BATHTUB
        #-------------------------------------------------------------
        
   
        self.bathtub = device("masterBathroom bathtub",dbCursor)
        self.bathtub.actuators.append(actuator("masterBathroom Bathtub Actuator","masterBathroom Bathtub",dbCursor))
        self.bathtub.sensors.append(liquidFlowSensor("MBBLFS","masterBathroom Bathtub",dbCursor))


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
    #   SINK
    #-------------------------------------------------------------
   
    #His Sink
    def turnOnSink(self):
        """Turns on the His sink."""
        self.sink.actuators[0].turnOn()

    def turnOffSink(self):
        """Turns off the His sink."""
        self.sink.actuators[0].turnOff()

    def getSinkState(self):
        """Returns the His sink's state (on/off)."""
        return self.sink.actuators[0].getState()

    def setSinkFlow(self, flowRate):
        """Sets the flow rate of the His sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.sink.sensors[0].setFlowRatePct(flowRate)

    def getSinkFlow(self):
        """Returns the His sink's flow rate."""
        return self.sink.sensors[0].getFlowRatePct()

    #Her Sink
    def turnOnherSink(self):
        """Turns on her sink."""
        self.hersink.actuators[0].turnOn()
    
    def turnOffherSink(self):
        """Turns off her sink."""
        self.hersink.actuators[0].turnOff()

    def getHerSinkState(self):
        """Gets her sink's state (on/off)."""
        return self.hersink.actuators[0].getState()

    def setherSinkFlow(self, flowRate):
        """Sets the flow rate of the her sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.hersink.sensors[0].setFlowRatePct(flowRate)

    def getherSinkFlow(self):
        """Returns the her sink's flow rate."""
        return self.hersink.sensors[0].getFlowRatePct()
    

    #-------------------------------------------------------------
    #   TOILET
    #-------------------------------------------------------------
    
    #His Toilet
    def turnOnToilet(self):
        """Turns on the His Toilet."""
        self.toilet.actuators[0].turnOn()

    def turnOfftoilet(self):
        """Turns off the His Toilet."""
        self.toilet.actuators[0].turnOff()

    def gettoiletState(self):
        """Returns the His Toilet's state (on/off)."""
        return self.toilet.actuators[0].getState()

    def settoiletFlow(self, flowRate):
        """Sets the flow rate of the His Toilet.

        Keyword Arguments:
        flowRate        -- the flow rate of the toilet as a percent of its maximum flow.

        """
        self.toilet.sensors[0].setFlowRatePct(flowRate)

    def gettoiletFlow(self):
        """Returns the His Toilet's flow rate."""
        return self.toilet.sensors[0].getFlowRatePct()

    #her toilet
    def turnOnhertoilet(self):
        """Turns on the her toilet."""
        self.toilet.actuators[0].turnOn()
    
    def turnOffhertoilet(self):
        """Turns off the toilet."""
        self.toilet.actuators[0].turnOff()

    def gethertoiletState(self):
        """Gets the toilet's state (on/off)."""
        return self.toilet.actuators[0].getState()

    def sethertoiletFlow(self, flowRate):
        """Sets the flow rate of the her toilet.

        Keyword Arguments:
        flowRate        -- the flow rate of the toilet as a percent of its maximum flow.

        """
        self.toilet.sensors[0].setFlowRatePct(flowRate)

    def gethertoiletFlow(self):
        """Returns the her toilet's flow rate."""
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


    test=masterBathroom("masterBathroom",cursor)

    test.openDoor(0)
    # test.setSmokeState(1)
    print(test.getTemp())


    db.commit()
    db.close()
main()  