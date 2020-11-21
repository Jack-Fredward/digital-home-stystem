#bedroom.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class bedRoom:
    def __init__(self, name, number, dbCursor, has_extDoor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("bedroom"+number+"Lights",dbCursor)
        self.lights.actuators.append(actuator("bedroom"+number+"Light Actuator","bedroom"+number+"Lights",dbCursor))
        self.lights.sensors.append(brightSensor("Bed"+number+"LBS","bedroom"+number+"Lights", dbCursor))
        self.lights.sensors.append(motionSensor("Bed"+number+"LMS","bedroom"+number+"Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS 
        #-------------------------------------------------------------

        self.doors = []
        self.doors.append(device("bedroom"+number+"door",dbCursor))
        self.doors[0].actuators.append(actuator("bedroom"+number+"Door Actuator", "bedroom"+number+"door",dbCursor))
        self.doors[0].sensors.append(openCloseSensors("Bed"+number+"DOCS","bedroom"+number+"door",dbCursor))

        if (has_extDoor == 1):
            self.doors.append(device("bedroom"+number+"ExtDoor",dbCursor))
            self.doors[0].actuators.append(actuator("bedroom"+number+"ExtDoor Actuator", "bedroom"+number+"ExtDoor",dbCursor))
            self.doors[0].sensors.append(openCloseSensors("Bed"+number+"EDOCS","bedroom"+number+"ExtDoor",dbCursor))
      
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("bedroom"+number+"window1",dbCursor))
        self.windows[0].actuators.append(actuator("bedroom"+number+"window1 Actuator", "bedroom"+number+"window1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("Bed"+number+"W1OCS","bedroom"+number+"window1",dbCursor))
        self.windows.append(device("bedroom"+number+"window2",dbCursor))
        self.windows[1].actuators.append(actuator("bedroom"+number+"window2 Actuator", "bedroom"+number+"window2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("Bed"+number+"W2OCS","bedroom"+number+"window2",dbCursor))

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("bedroom"+number+ "AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("Bed"+number+"ACTS","bedroom"+number+"AirCon",dbCursor))
        self.aircon.actuators.append(actuator("bedroom"+number+"AirCon Actuator","bedroom"+number+"AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("bedroom"+number+"Heat",dbCursor)
        self.heat.actuators.append(actuator("bedroom"+number+"Heat Actuator","bedroom"+number+"Heat",dbCursor))
        self.heat.sensors.append(tempSensor("Bed"+number+"HTS","bedroom"+number+"Heat",dbCursor))
        self.setHeatTemp(ROOMTEMP)

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        # NO CAMERAS

       


    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    def turnOnLights(self,frame,db):
        self.lights.actuators[0].turnOn()
        frame.bedroomLightsStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()
    
    def turnOffLights(self,frame,db):
        self.lights.actuators[0].turnOff()
        self.setLightBrightness(frame, 0, db)
        frame.bedroomLightsStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()
    
    def getLightsState(self):
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,frame,bright,db):
        self.lights.sensors[0].setBrightPct(bright)
        if bright!=0:
            self.turnOnLights(frame,db)
        frame.bedroomLightsBrightValueDisplayLabel.config(text=str(bright)+"%")
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

    def openDoor(self,doorNum,frame,db):
        self.doors[doorNum].actuators[0].turnOn()
        self.doors[doorNum].sensors[0].updateOpen()
        frame.doorStateDisplayLabel[doorNum].config(text="Open")
        frame.update()
        db.commit()


    def closeDoor(self,doorNum,frame,db):
        self.doors[doorNum].actuators[0].turnOff()
        self.doors[doorNum].sensors[0].updateClosed()
        frame.doorStateDisplayLabel[doorNum].config(text="Closed")
        frame.update()
        db.commit()

    def getDoorState(self,doorNum):
        return self.doors[doorNum].actuators[0].getState()

    def getDoorOpenCloseState(self,doorNum):
        return self.doors[doorNum].sensors[0].getState()



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

#     bedRoom2 = bedRoom("bedroom2", "2", cursor, 0)
#     bedRoom3 = bedRoom("bedroom3", "3", cursor, 0)
#     bedRoom4 = bedRoom("bedroom4", "4", cursor, 1)

#     db.commit()
#     db.close()
# main()  
