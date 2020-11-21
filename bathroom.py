#bathroom1.py

import pymysql
from device import *
import datetime
import time

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
            self.doors[1].actuators.append(actuator("Bathroom"+number+"ExtDoor Actuator", "Bathroom"+number+"ExtDoor",dbCursor))
            self.doors[1].sensors.append(openCloseSensors("B"+number+"EDOCS","Bathroom"+number+"ExtDoor",dbCursor))
      
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
            self.shower.actuators.append(actuator("Bathroom"+number+"Shower Actuator","Bathroom"+number+"shower",dbCursor))
            self.shower.sensors.append(liquidFlowSensor("B"+number+"SHLFS","Bathroom"+number+"shower",dbCursor))
            self.shower.sensors.append(tempSensor("B"+number+"SHTS","Bathroom"+number+"shower",dbCursor))
        #-------------------------------------------------------------
        #   BATHTUB
        #-------------------------------------------------------------
        
        if (has_bathtub == 1):
            self.bathtub = device("Bathroom"+number+"bathtub",dbCursor)
            self.bathtub.actuators.append(actuator("Bathroom"+number+"Bathtub Actuator","Bathroom"+number+"bathtub",dbCursor))
            self.bathtub.sensors.append(liquidFlowSensor("B"+number+"BLFS","Bathroom"+number+"bathtub",dbCursor))
            self.bathtub.sensors.append(tempSensor("B"+number+"BTS","Bathroom"+number+"bathtub",dbCursor))

    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    def turnOnLights(self,frame,db):
        self.lights.actuators[0].turnOn()
        frame.bathroomLightsStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()
    
    def turnOffLights(self,frame,db):
        self.lights.actuators[0].turnOff()
        self.setLightBrightness(frame, 0, db)
        frame.bathroomLightsStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()
    
    def getLightsState(self):
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,frame,bright,db):
        self.lights.sensors[0].setBrightPct(bright)
        if bright!=0:
            self.turnOnLights(frame,db)
        frame.bathroomLightsBrightValueDisplayLabel.config(text=str(bright)+"%")
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
        frame.doorStateDisplayLabel[0].config(text="Open")
        frame.update()
        db.commit()


    def closeDoor(self,doorNum,frame,db):
        self.doors[doorNum].actuators[0].turnOff()
        self.doors[doorNum].sensors[0].updateClosed()
        frame.doorStateDisplayLabel[0].config(text="Closed")
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

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------
   
    def turnOnSink(self,frame,db):
        self.sink.actuators[0].turnOn()
        frame.bathroomSinkStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffSink(self,frame,db):
        self.sink.actuators[0].turnOff()
        self.setSinkFlow(frame, 0,db)
        frame.bathroomSinkStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getSinkState(self):
        return self.sink.actuators[0].getState()

    def setSinkFlow(self, frame,flowRate,db):
        self.sink.sensors[0].setFlowRatePct(flowRate)
        if flowRate!=0:
            self.turnOnSink(frame, db)
        frame.bathroomSinkFlowValueDisplayLabel.config(text = str(flowRate)+"%")
        frame.update()
        db.commit()

    def getSinkFlow(self):
        return self.sink.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   TOILET
    #-------------------------------------------------------------
    
    def turnOnToilet(self,frame,flowRate,db):
        self.toilet.actuators[0].turnOn()
        self.setToiletFlow(frame,flowRate,db)
        frame.BathroomToiletStateDisplayLabel.config(text="On")
        frame.update()
        time.sleep(2)
        self.turnOffToilet(frame,db)
        db.commit()

    def turnOffToilet(self,frame,db):
        self.toilet.actuators[0].turnOff()
        self.setToiletFlow(frame, 0,db)
        frame.BathroomToiletStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getToiletState(self):
        return self.toilet.actuators[0].getState()

    def setToiletFlow(self, frame,flowRate,db):
        self.toilet.sensors[0].setFlowRatePct(flowRate)
        frame.toiletFlowLabel.config(text="Flow Rate: "+str(flowRate)+"%")
        frame.update()
        db.commit()

    def getToiletFlow(self):
        return self.toilet.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   SHOWER
    #-------------------------------------------------------------
    
    def turnOnShower(self,frame,db):
        self.shower.actuators[0].turnOn()
        frame.bathroomShowerStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffShower(self,frame,db):
        self.shower.actuators[0].turnOff()
        self.setShowerFlow(frame,0,0,db)
        self.setShowerTemp(frame,0,db)
        frame.bathroomShowerStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getShowerState(self):
        return self.shower.actuators[0].getState()

    def setShowerFlow(self, frame,flowRate,temp,db):
        self.shower.sensors[0].setFlowRatePct(flowRate)
        if flowRate!=0:
            self.turnOnShower(frame,db)
            self.setShowerTemp(frame,temp,db)
        frame.bathroomShowerFlowValueDisplayLabel.config(text=str(flowRate)+"%")
        frame.update()
        db.commit()


    def getShowerFlow(self):
        return self.shower.sensors[0].getFlowRatePct()

    def setShowerTemp(self,frame,temp,db):
       self.shower.sensors[1].setTemp(temp)
       frame.showerTempValueDisplayLabel.config(text="Temp(*F): "+str(temp))
       frame.update()
       db.commit()

    def getShowerTemp(self):
        self.shower.sensors[1].getTemp()

    #-------------------------------------------------------------
    #   BATHTUB
    #-------------------------------------------------------------

    def turnOnBathtub(self,frame,db):
        self.bathtub.actuators[0].turnOn()
        frame.bathroomBathtubStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffBathtub(self,frame,db):
        self.bathtub.actuators[0].turnOff()
        self.setBathtubFlow(frame,0,0,db)
        self.setBathtubTemp(frame,0,db)
        frame.bathroomBathtubStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getBathtubState(self):
        return self.bathtub.actuators[0].getState()

    def setBathtubFlow(self, frame,flowRate,temp,db):
        self.bathtub.sensors[0].setFlowRatePct(flowRate)
        if flowRate!=0:
            self.turnOnBathtub(frame,db)
            self.setBathtubTemp(frame,temp,db)
        frame.bathroomBathtubFlowValueDisplayLabel.config(text=str(flowRate)+"%")
        frame.update()
        db.commit()


    def getBathtubFlow(self):
        return self.bathtub.sensors[0].getFlowRatePct()

    def setBathtubTemp(self,frame,temp,db):
       self.bathtub.sensors[1].setTemp(temp)
       frame.bathtubTempValueDisplayLabel.config(text="Temp(*F): "+str(temp))
       frame.update()
       db.commit()

    def getBathtubTemp(self):
        self.bathtub.sensors[1].getTemp()

    

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