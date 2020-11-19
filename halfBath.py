#Half_Bath.py


import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class halfBathroom:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("halfBathroom Lights",dbCursor)
        self.lights.actuators.append(actuator("halfBathroom Light Actuator","halfBathroom Lights",dbCursor))
        self.lights.sensors.append(brightSensor("HBLBS","halfBathroom Lights", dbCursor))
        self.lights.sensors.append(motionSensor("HBLMS","halfBathroom Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("halfBathroom door",dbCursor))
        self.doors[0].actuators.append(actuator("halfBathroom Door Actuator", "halfBathroom door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("HBDOCS","halfBathroom door",dbCursor))

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
        self.aircon = device("halfBathroom AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("HBACTS","halfBathroom AirCon",dbCursor))
        self.aircon.actuators.append(actuator("halfBathroom AirCon Actuator","halfBathroom AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("halfBathroom Heat",dbCursor)
        self.heat.actuators.append(actuator("halfBathroom Heat Actuator","halfBathroom Heat",dbCursor))
        self.heat.sensors.append(tempSensor("HBHTS","halfBathroom Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("halfBathroom Sink", dbCursor)
        self.sink.actuators.append(actuator("halfBathroom Sink Actuator","halfBathroom Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("HBSLFS","halfBathroom Sink",dbCursor))
       
     
        #-------------------------------------------------------------
        #   TOILET
        #-------------------------------------------------------------
        
        self.toilet = device("halfBathroom Toilet", dbCursor)
        self.toilet.actuators.append(actuator("halfBathroom Toilet Actuator","halfBathroom Toilet",dbCursor))
        self.toilet.sensors.append(liquidFlowSensor("HBTLFS","halfBathroom Toilet",dbCursor))



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


# def main():
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


#     test=halfBathroom("halfBathroom",cursor)

#     test.openDoor(0)
#     print(test.getTemp())

#     db.commit()
#     db.close()

# main()