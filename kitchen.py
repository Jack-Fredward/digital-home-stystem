#kitchen.py

import pymysql
from device import *
import datetime


# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class kitchen:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor
        

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #-------------------------------------------------------------
        #   OVEN
        #-------------------------------------------------------------
        self.OVENDELTAT = 100 #100 degrees per second
        self.oven = device("Oven",dbCursor)
        self.oven.sensors.append(tempSensor("OTS1","Oven",dbCursor))
        self.oven.actuators.append(actuator("Oven Actuator", "Oven",dbCursor))

        #-------------------------------------------------------------
        #   FRIDGE
        #-------------------------------------------------------------
        self.fridge = device("Fridge",dbCursor)
        self.fridge.sensors.append(tempSensor("FTS1","Fridge",dbCursor))
        self.fridge.sensors.append(openCloseSensors("Fridge Door OCS","Fridge",dbCursor))

        #-------------------------------------------------------------
        #   STOVE
        #-------------------------------------------------------------

        self.STOVEDELTAT = 50 #50 degrees per second
        self.stove = device("Stove",dbCursor)
        for i in range(4):
            self.stove.sensors.append(tempSensor("STS"+str(i+1),"Stove",dbCursor))
            self.stove.actuators.append(actuator("Burner"+str(i+1)+" Actuator","Stove",dbCursor))

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------
        #Kitchen Sink
        self.sink = device("Sink", dbCursor)
        self.sink.actuators.append(actuator("Sink Actuator","Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("SLFS","Sink",dbCursor))

        #Pantry Sink
        self.pantrysink = device("Pantry Sink",dbCursor)
        self.pantrysink.actuators.append(actuator("Pantry Sink Actuator", "Pantry Sink", dbCursor))
        self.pantrysink.sensors.append(liquidFlowSensor("PSLFS","Pantry Sink", dbCursor))
        #-------------------------------------------------------------
        #   MICROWAVE
        #-------------------------------------------------------------

        self.microwave = device("Microwave",dbCursor)
        self.microwave.actuators.append(actuator("Microwave Actuator", "Microwave", dbCursor))
        self.microwave.sensors.append(tempSensor("MTS", "Microwave",dbCursor))

        #-------------------------------------------------------------
        #   DISH WASHER
        #-------------------------------------------------------------

        self.DISHWASHERCAP = 50 #Arbitrary number of dishes the dishwasher can hold
        self.dishwasherDishCount = 0
        self.dishwasher = device("Dishwasher",dbCursor)
        self.dishwasher.actuators.append(actuator("Dishwasher Actuator", "Dishwasher", dbCursor))
        self.dishwasher.sensors.append(liquidFlowSensor("DWLFS","Dishwasher", dbCursor))

        #-------------------------------------------------------------
        #   COFFEE MAKER
        #-------------------------------------------------------------

        self.coffeemaker = device("Coffee Maker",dbCursor)
        self.coffeemaker.actuators.append(actuator("Coffee Maker Actuator", "Coffee Maker",dbCursor))
        self.coffeemaker.sensors.append(tempSensor("CMTS","Coffee Maker",dbCursor))
        self.coffeemaker.sensors.append(liquidFlowSensor("CMLFS","Coffee Maker",dbCursor))

        #-------------------------------------------------------------
        #   TOASTER
        #-------------------------------------------------------------

        self.toaster = device("Toaster", dbCursor)
        self.toaster.actuators.append(actuator("Toaster Actuator", "Toaster", dbCursor))
        self.toaster.sensors.append(tempSensor("TTS","Toaster",dbCursor))

        #-------------------------------------------------------------
        #   GARBAGE DISPOSAL
        #-------------------------------------------------------------

        self.garbagedisposal = device("Garbage Disposal",dbCursor)
        self.garbagedisposal.actuators.append(actuator("Garbage Disposal Actuator", "Garbage Disposal",dbCursor))

        #-------------------------------------------------------------
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Kitchen Lights",dbCursor)
        self.lights.actuators.append(actuator("Kitchen Light Actuator","Kitchen Lights",dbCursor))
        self.lights.sensors.append(brightSensor("KLBS","Kitchen Lights", dbCursor))
        self.lights.sensors.append(motionSensor("KLMS","Kitchen Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS
        #-------------------------------------------------------------

        #   NO DOORS
        
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------
        #WINDOWS DONT NEED SENSORS THE ACTUATOR CAN REPRESENT THE STATE OF THE DOOR
        self.windows = []
        self.windows.append(device("KWindow1",dbCursor))
        self.windows[0].actuators.append(actuator("Kitchen Window 1 Actuator", "Kwindow1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("KW1OCS","KWindow1",dbCursor))
        self.windows.append(device("KWindow2",dbCursor))
        self.windows[1].actuators.append(actuator("Kitchen Window 2 Actuator", "Kwindow2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("KW2OCS","KWindow2",dbCursor))
        
        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------
        ROOMTEMP = 70 #70 degrees F average for standard room temp
        #AC
        self.ACDELTAT = -1 #cools off by 1 degree a second
        self.aircon = device("Kitchen AirCon",dbCursor)
        self.aircon.sensors.append(tempSensor("KACTS","Kitchen AirCon",dbCursor))
        self.aircon.actuators.append(actuator("Kitchen AirCon Actuator","Kitchen AirCon",dbCursor))
        self.setACTemp(ROOMTEMP)

        #HEAT
        self.HEATDELTAT = 1 #heats up by 1 degree a second
        self.heat = device("Kitchen Heat",dbCursor)
        self.heat.actuators.append(actuator("Kitchen Heat Actuator","Kitchen Heat",dbCursor))
        self.heat.sensors.append(tempSensor("KHTS","Kitchen Heat",dbCursor))
        print(self.heat.sensors[0].getTemp())
        self.setHeatTemp(ROOMTEMP)
        print(self.heat.sensors[0].getTemp())


        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------
        
        self.cameras = []
        self.cameras.append(device("Kitchen Camera 1",dbCursor))
        self.cameras[0].actuators.append(actuator("Kitchen Camera 1 Actuator","Kitchen Camera 1",dbCursor))
        self.cameras[0].sensors.append(motionSensor("KC1MS","Kitchen Camera 1",dbCursor))

        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokeDetector=device("Kitchen Smoke Detector",dbCursor)
        self.smokeDetector.actuators.append(actuator("Kitchen Smoke Detector Actuator","Kitchen Smoke Detecor", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("KSDOCS", "Kitchen Smoke Detector",dbCursor))
        
    
    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   OVEN
    #-------------------------------------------------------------

    def turnOnOven(self):
        self.oven.actuators[0].turnOn()

    def turnOffOven(self):
        self.oven.actuators[0].turnOff()

    def getOvenTemp(self):
        return self.oven.sensors[0].getTemp()

    def setOvenTemp(self,temp):
        self.oven.sensors[0].setTemp(temp)

    def updateOvenTemp(self):
        # lut = self.oven.actuators[0].getLUT()
        # now = datetime.datetime.now()
        # timeDiff = now - lut
        # secondsElapsed = round(timeDiff.total_seconds())
        # self.setOvenTemp((secondsElapsed*self.OVENDELTAT))
        self.setOvenTemp(self.getOvenTemp()+self.OVENDELTAT)

    def getOvenState(self):
        return self.oven.actuators[0].getState()

    #-------------------------------------------------------------
    #   FRIDGE
    #-------------------------------------------------------------

    def turnOnFridge(self):
        self.fridge.actuators[0].turnOn()

    def turnOffFridge(self):
        self.fridge.actuators[0].turnOff()

    def getFridgeState(self):
        return self.fridge.actuators[0].getState()
    
    def openFridgeDoor(self):
        self.fridge.sensors[0].updateOpen()

    def closeFridgeDoor(self):
        self.fridge.sensors[0].updateClosed()

    def getFridgeDoorState(self):
        return self.fridge.sensors[0].getState()
    
    #-------------------------------------------------------------
    #   STOVE
    #-------------------------------------------------------------

    def turnOnStoveBurner(self, burnerNum):
        self.stove.actuators[burnerNum].turnOn()

    def turnOffStoveBurner(self, burnerNum):
        self.stove.actuators[burnerNum].turnOff()

    def getStoveBurnerTemp(self, burnerNum):
        return self.stove.sensors[burnerNum].getTemp()

    def getStoveBurnerState(self, burnerNum):
        return self.stove.actuators[burnerNum].getState()

    def setStoveBurnerTemp(self, burnerNum, temp):
        self.stove.sensors[burnerNum].setTemp(temp)

    def updateStoveBurnerTemp(self,burnerNum):
        # lut = self.stove.actuators[burnerNum].getLUT()
        # now = datetime.datetime.now()
        # timeDiff = now - lut
        # secondsElapsed = round(timeDiff.total_seconds())
        self.setStoveBurnerTemp(burnerNum,(self.getStoveBurnerTemp(burnerNum)+self.STOVEDELTAT))

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------

    #Kitchen Sink
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
    
    #Pantry Sink
    def turnOnPantrySink(self):
        self.pantrysink.actuators[0].turnOn()
    
    def turnOffPantrySink(self):
        self.pantrysink.actuators[0].turnOff()

    def getPantrySinkState(self):
        return self.pantrysink.actuators[0].getState()

    def setPantrySinkFlow(self, flowRate):
        self.pantrysink.sensors[0].setFlowRatePct(flowRate)

    def getPantrySinkFlow(self):
        return self.pantrysink.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   MICROWAVE
    #-------------------------------------------------------------

    def turnOnMicrowave(self):
        self.microwave.actuators[0].turnOn()

    def turnOffMicrowave(self):
        self.microwave.actuators[0].turnOff()

    def getMicrowaveState(self):
        return self.microwave.actuators[0].getState()

    def setMicrowaveTemp(self, temp):
        self.microwave.sensors[0].setTemp(temp)

    def getMicrowaveTemp(self):
        return self.microwave.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   DISH WASHER
    #-------------------------------------------------------------

    def turnOnDishwasher(self):
        self.dishwasher.actuators[0].turnOn()

    def turnOffDishwaser(self):
        self.dishwasher.actuators[0].turnOff()

    def getDishwasherState(self):
        return self.microwave.actuators[0].getState()

    def setDishwasherFlow(self, flowRate):
        self.dishwasher.sensors[0].setFlowRatePct(flowRate)

    def getDishwasherFlow(self):
        return self.dishwasher.sensors[0].getFlowRatePct()

    def getDishwasherCap(self):
        return self.DISHWASHERCAP

    def getDishwasherDishCount(self):
        return self.dishwasherDishCount
    
    def addDishToDishwasher(self,numDishes):
        if(self.getDishwasherDishCount()+numDishes<=self.DISHWASHERCAP):
            self.dishwasherDishCount+=numDishes
        else:
            print("Too many dishes. Must add less")

    

    #-------------------------------------------------------------
    #   COFFEE MAKER
    #-------------------------------------------------------------

    def turnOnCoffeeMaker(self):
        self.coffeemaker.actuators[0].turnOn()

    def turnOffCofeeMaker(self):
        self.coffeemaker.actuators[0].turnOff()

    def getCoffeeMakerState(self):
        return self.coffeemaker.actuators[0].getState()
    
    def setCoffeeMakerFlow(self, flowRate):
        self.coffeemaker.sensors[1].setFlowRatePct(flowRate)
    
    def getCoffeMakerFlow(self):
        return self.coffeemaker.sensors[1].getFlowRatePct()

    def setCoffeeMakerTemp(self, temp):
        self.coffeemaker.sensors[0].setTemp(temp)

    def getCoffeeMakerTemp(self):
        return self.coffeemaker.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   TOASTER
    #-------------------------------------------------------------

    def turnOnToaster(self):
        self.toaster.actuators[0].turnOn()

    def turnOffToaster(self):
        self.toaster.actuators[0].turnOff()

    def getToasterState(self):
        return self.toaster.actuators[0].getState()

    def setToasterTemp(self, temp):
        self.toaster.sensors[0].setTemp(temp)

    def getToasterTemp(self):
        self.toaster.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   GARBAGE DISPOSAL
    #-------------------------------------------------------------

    def turnOnGarbageDisposal(self):
        self.garbagedisposal.actuators[0].turnOn()

    def turnOffGarbageDisposal(self):
        self.garbagedisposal.actuators[0].turnOff()

    def getGarbageDisposalState(self):
        return self.garbagedisposal.actuators[0].getState()

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
  
    #   NO DOORS
  
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
    #   CAMERAS
    #-------------------------------------------------------------

    def turnOnCamera(self, camNum):
        self.cameras[camNum].actuators[0].turnOn()

    def turnOffCamera(self, camNum):
        self.cameras[camNum].actuators[0].turnOff()

    def getCameraState(self, camNum):
        return self.cameras[camNum].actuators[0].getState()

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

# def main():
#     # Open database connection
#     db = pymysql.connect("localhost","jp","Database","digital_home_database" )

#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
    
#     cursor.execute("DELETE FROM TempSensors")
#     cursor.execute("DELETE FROM OpenCloseSensors")
#     cursor.execute("DELETE FROM MotionSensors")
#     cursor.execute("DELETE FROM LiquidFlowSensors")
#     cursor.execute("DELETE FROM BrightnessSensor")
#     cursor.execute("DELETE FROM Actuators")
#     cursor.execute("DELETE FROM Devices")

#     # oven = device("Oven",cursor)

#     # tempS = tempSensor("TS1","Oven",cursor)

#     # oven.sensors.append(tempS)

#     # kitchen = room("kitchen",cursor)

#     # kitchen.devices.append(oven)
#     # print(kitchen.devices[0].getName())
#     kitchen1 = kitchen("Kitchen", cursor)
#     print(kitchen1.oven.actuators[0].getState())
#     kitchen1.turnOnOven()
#     print(kitchen1.oven.actuators[0].getState())
#     kitchen1.turnOffOven()
#     print(kitchen1.oven.actuators[0].getState())
#     print("FRIDGE")
#     print(kitchen1.getFridgeDoorState())
#     kitchen1.openFridgeDoor()
#     print(kitchen1.getFridgeDoorState())
#     kitchen1.closeFridgeDoor()
#     print(kitchen1.getFridgeDoorState())



#     db.commit()
#     db.close()
# main()