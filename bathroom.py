#bathroom1.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class bathroom:
    def __init__(self, name, number, dbCursor, has_shower, has_bathtub, has_extDoor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Bathroom"+number+"Lights",dbCursor)
        self.lights.actuators.append(actuator("Bathroom"+number+"Light Actuator","Bathroom"+number+"Lights",dbCursor))
        self.lights.sensors.append(brightSensor("B"+number+"LBS","Bathroom"+number+"Lights", dbCursor))
        self.lights.sensors.append(motionSensor("B"+number+"LMS","Bathroom"+number+"Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("Bathroom"+number+"door",dbCursor))
        self.doors[0].actuators.append(actuator("Bathroom"+number+"Door Actuator", "Bathroom"+number+"door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("B"+number+"DOCS","Bathroom"+number+"door",dbCursor))

        if (has_extDoor == 1):
            self.doors.append(device("Bathroom"+number+"ExtDoor",dbCursor))
            self.doors[0].actuators.append(actuator("Bathroom"+number+"ExtDoor Actuator", "Bathroom"+number+"ExtDoor",dbCursor))
            self.doors[0].sensors.append(openCloseSensors("B"+number+"EDOCS","Bathroom"+number+"ExtDoor",dbCursor))
      
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("Bathroom"+number+"window",dbCursor))
        self.windows[0].actuators.append(actuator("Bathroom"+number+"window Actuator", "Bathroom"+number+"window",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("B"+number+"WOCS","Bathroom"+number+"window",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("Bathroom"+number+ "AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("B"+number+"ACTS","Bathroom"+number+"AirCon",dbCursor))
        self.aircon.actuators.append(actuator("Bathroom"+number+"AirCon Actuator","Bathroom"+number+"AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("Bathroom"+number+"Heat",dbCursor)
        self.heat.actuators.append(actuator("Bathroom"+number+"Heat Actuator","Bathroom"+number+"Heat",dbCursor))
        self.heat.sensors.append(tempSensor("B"+number+"HTS","Bathroom"+number+"Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("Bathroom"+number+"Sink", dbCursor)
        self.sink.actuators.append(actuator("Bathroom"+number+"Sink Actuator","Bathroom"+number+"Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("B"+number+"SLFS","Bathroom"+number+"Sink",dbCursor))
       
        #-------------------------------------------------------------
        #   TOILET
        #-------------------------------------------------------------
        
        self.toilet = device("Bathroom"+number+"Toilet", dbCursor)
        self.toilet.actuators.append(actuator("Bathroom"+number+"Toilet Actuator","Bathroom"+number+"Toilet",dbCursor))
        self.toilet.sensors.append(liquidFlowSensor("B"+number+"TLFS","Bathroom"+number+"Toilet",dbCursor))

        #-------------------------------------------------------------
        #   SHOWER
        #-------------------------------------------------------------

        if (has_shower == 1):
            self.shower = device("Bathroom"+number+"shower",dbCursor)
            self.shower.actuators.append(actuator("Bathroom"+number+"Shower Actuator","Bathroom"+number+"Shower",dbCursor))
            self.shower.sensors.append(liquidFlowSensor("B"+number+"SHLFS","Bathroom"+number+"Shower",dbCursor))
        #-------------------------------------------------------------
        #   BATHTUB
        #-------------------------------------------------------------
        
        if (has_bathtub == 1):
            self.bathtub = device("Bathroom"+number+"bathtub",dbCursor)
            self.bathtub.actuators.append(actuator("Bathroom"+number+"Bathtub Actuator","Bathroom"+number+"Bathtub",dbCursor))
            self.bathtub.sensors.append(liquidFlowSensor("B"+number+"BLFS","Bathroom"+number+"Bathtub",dbCursor))


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
    #   TOILET
    #-------------------------------------------------------------
    
    def turnOnToilet(self):
        self.toilet.actuators[0].turnOn()

    def turnOffToilet(self):
        self.toilet.actuators[0].turnOff()

    def getToiletState(self):
        return self.toilet.actuators[0].getState()

    def setToiletFlow(self, flowRate):
        self.toilet.sensors[0].setFlowRatePct(flowRate)

    def getToiletFlow(self):
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

    

# def main ():

#     # Open database connection
#     db = pymysql.connect("localhost","root","Audrey1!seed","digitalhome" )
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

#     bathroom2 = bathroom("Bathroom2", "2", cursor,0,0,0)
#     bathroom3 = bathroom("Bathroom3", "3", cursor,0,1,0)
#     bathroom4 = bathroom("Bathroom4", "4", cursor,1,0,1)




    

#     db.commit()
#     db.close()
# main()  