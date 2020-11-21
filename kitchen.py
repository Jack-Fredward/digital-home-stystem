#kitchen.py

import pymysql
from device import *
import datetime

class kitchen:
    """A digital home kitchen."""
    def __init__(self, name, dbCursor):
        """"Initiallizing a kitchen. Creates all the kitchen devices. The kitchen has the following devices:
        Oven
        Fridge
        Stove
        Kitchen Sink
        Pantry Sink
        Microwave
        Dish Washer
        Coffee Maker
        Toaster
        Garbage Disposal
        Lights
        AC/Heat
        Smoke Detector

        
        Keyword arguments:
        name        --  the name of the kitchen
        dbCursor    --  the connection to the database
        
        """
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
        self.fridge.actuators.append(actuator("Fridge Actuator","Fridge",dbCursor))
        self.fridge.sensors.append(openCloseSensors("FDOCS","Fridge",dbCursor))
        self.fridge.actuators[0].turnOn()

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
        self.sink = device("Kitchen Sink", dbCursor)
        self.sink.actuators.append(actuator("Sink Actuator","Kitchen Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("KSLFS","Kitchen Sink",dbCursor))

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

        #self.DISHWASHERCAP = 50 #Arbitrary number of dishes the dishwasher can hold
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

        #   NO WINDOWS
        
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
        self.setHeatTemp(ROOMTEMP)


        #-------------------------------------------------------------
        #   SMOKE DETECTOR
        #-------------------------------------------------------------

        self.smokeDetector=device("Kitchen Smoke Detector",dbCursor)
        self.smokeDetector.actuators.append(actuator("Kitchen Smoke Detector Actuator","Kitchen Smoke Detector", dbCursor))
        self.smokeDetector.sensors.append(openCloseSensors("KSDOCS", "Kitchen Smoke Detector",dbCursor))
        self.turnOnSmokeDetector()
        
    
    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   OVEN
    #-------------------------------------------------------------

    def turnOnOven(self,frame):
        """"Turns on the oven."""
        self.oven.actuators[0].turnOn()
        frame.ovenStateDisplayLabel.config(text="On")
        frame.update()


    def turnOffOven(self,frame):
        """Turns off the oven."""
        self.oven.actuators[0].turnOff()
        frame.ovenStateDisplayLabel.config(text="Off")
        frame.update()

    def getOvenTemp(self):
        """Returns the oven temp."""
        return self.oven.sensors[0].getTemp()

    def setOvenTemp(self,temp):
        """Sets the oven temp.

        Keyword Arguments:
        temp        -- the temp of the oven in degrees F.
        """
        self.oven.sensors[0].setTemp(temp)

    def updateOvenTemp(self):
        """Updates the oven temp."""
        self.setOvenTemp(self.getOvenTemp()+self.OVENDELTAT)

    def getOvenState(self):
        """Returns the oven's state (on/off)."""
        return self.oven.actuators[0].getState()

    #-------------------------------------------------------------
    #   FRIDGE
    #-------------------------------------------------------------

    def turnOnFridge(self,frame,db):
        """Turns on the fridge."""
        self.fridge.actuators[0].turnOn()
        frame.fridgeStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffFridge(self,frame,db):
        """Turns off the fridge."""
        self.fridge.actuators[0].turnOff()
        frame.fridgeStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getFridgeState(self):
        """Returns the fridge's state (on/off)."""
        return self.fridge.actuators[0].getState()
    
    def openFridgeDoor(self,frame,db):
        """Opens the fridge door."""
        self.fridge.sensors[0].updateOpen()
        frame.fridgeDoorStateDisplayLabel.config(text="Open")
        frame.update()
        db.commit()

    def closeFridgeDoor(self,frame,db):
        """Closes the fridge door."""
        self.fridge.sensors[0].updateClosed()
        frame.fridgeDoorStateDisplayLabel.config(text="Closed")
        frame.update()
        db.commit()

    def getFridgeDoorState(self):
        """Returns the fridge door's state (open/close)."""
        return self.fridge.sensors[0].getState()
    
    #-------------------------------------------------------------
    #   STOVE
    #-------------------------------------------------------------

    def turnOnStoveBurner(self,frame, burnerNum, db):
        """Turns on the Stove burner.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        self.stove.actuators[burnerNum].turnOn()
        frame.burnerStateDisplayLabel[burnerNum].config(text="On")
        frame.update()
        db.commit()

    def turnOffStoveBurner(self, frame,burnerNum,db):
        """Turns off the Stove burner.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        self.stove.actuators[burnerNum].turnOff()
        frame.burnerStateDisplayLabel[burnerNum].config(text="Off")
        frame.update()
        db.commit()

    def getStoveBurnerTemp(self, burnerNum):
        """Returns the temp of the Stove burner.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        return self.stove.sensors[burnerNum].getTemp()

    def getStoveBurnerState(self, burnerNum):
        """Returns the state of the Stove burner (on/off).

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        return self.stove.actuators[burnerNum].getState()

    def setStoveBurnerTemp(self, burnerNum, temp):
        """Sets the temperature of the Stove burner.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.
        temp            -- the temp in degrees F.

        """
        self.stove.sensors[burnerNum].setTemp(temp)

    def updateStoveBurnerTemp(self,burnerNum):
        """Updates the Stove burner's temp.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        self.setStoveBurnerTemp(burnerNum,(self.getStoveBurnerTemp(burnerNum)+self.STOVEDELTAT))

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------

    #Kitchen Sink
    def turnOnSink(self,frame,db):
        """Turns on the kitchen sink."""
        self.sink.actuators[0].turnOn()
        frame.kitchenSinkStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffSink(self,frame,db):
        """Turns off the kitchen sink."""
        self.sink.actuators[0].turnOff()
        self.setSinkFlow(frame, 0,db)
        frame.kitchenSinkStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getSinkState(self):
        """Returns the kitchen sink's state (on/off)."""
        return self.sink.actuators[0].getState()

    def setSinkFlow(self, frame, flowRate, db):
        """Sets the flow rate of the kitchen sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.sink.sensors[0].setFlowRatePct(flowRate)
        if flowRate != 0:
            self.turnOnSink(frame, db)
        frame.kitchenSinkFlowValueDisplayLabel.config(text = str(flowRate)+"%")
        frame.update()
        db.commit()


    def getSinkFlow(self):
        """Returns the kitchen sink's flow rate."""
        return self.sink.sensors[0].getFlowRatePct()
    
    #Pantry Sink
    def turnOnPantrySink(self,frame,db):
        """Turns on the pantry sink."""
        self.pantrysink.actuators[0].turnOn()
        frame.pantrySinkStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()
    
    def turnOffPantrySink(self,frame,db):
        """Turns off the pantry sink."""
        self.pantrysink.actuators[0].turnOff()
        self.setPantrySinkFlow(frame,0,db)
        frame.pantrySinkStateDisplayLabel.config(text="Off")
        frame.update()

    def getPantrySinkState(self):
        """Gets the panty sink's state (on/off)."""
        return self.pantrysink.actuators[0].getState()

    def setPantrySinkFlow(self,frame, flowRate,db):
        """Sets the flow rate of the pantry sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.pantrysink.sensors[0].setFlowRatePct(flowRate)
        if flowRate!=0:
            self.turnOnPantrySink(frame,db)
        frame.pantrySinkFlowValueDisplayLabel.config(text = str(flowRate)+"%")
        frame.update()
        db.commit()

    def getPantrySinkFlow(self):
        """Returns the pantry sink's flow rate."""
        return self.pantrysink.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   MICROWAVE
    #-------------------------------------------------------------

    def turnOnMicrowave(self,frame,db):
        """Turns on the microwave."""
        self.microwave.actuators[0].turnOn()
        frame.microwaveStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffMicrowave(self,frame,db):
        """Turns off the microwave"""
        self.microwave.actuators[0].turnOff()
        frame.microwaveStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getMicrowaveState(self):
        """Returns the microwave's state (on/off)."""
        return self.microwave.actuators[0].getState()

    def setMicrowaveTemp(self, temp):
        """Sets the microwave's temp.

        Keyword Arguments:
        temp        -- the temperature in degrees F.

        """
        self.microwave.sensors[0].setTemp(temp)

    def getMicrowaveTemp(self):
        """Returns the microwaves temp."""
        return self.microwave.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   DISH WASHER
    #-------------------------------------------------------------

    def turnOnDishwasher(self,frame,db):
        """Turns on the dishwasher."""
        self.dishwasher.actuators[0].turnOn()
        frame.dishWasherStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffDishwasher(self,frame,db):
        """Turns off the dishwasher."""
        self.dishwasher.actuators[0].turnOff()
        frame.dishWasherStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getDishwasherState(self):
        """Returns the dishwasher's state (on/off)."""
        return self.dishwasher.actuators[0].getState()

    def setDishwasherFlow(self, flowRate):
        """Sets the flow rate of the dishwasher.

        Keyword Arguments:
        flowRate        -- the flow rate of the dishwasher as a percent of its maximum flow.

        """        
        self.dishwasher.sensors[0].setFlowRatePct(flowRate)

    def getDishwasherFlow(self):
        """Returns the dishwasher's flow rate."""
        return self.dishwasher.sensors[0].getFlowRatePct()

    # def getDishwasherCap(self):
    #     """Returns the dishwasher's max dish capacity."""
    #     return self.DISHWASHERCAP

    def getDishwasherDishCount(self):
        """Returns the dishwasher's dish count."""
        return self.dishwasherDishCount
    
    def addDishToDishwasher(self,numDishes):
        """Adds dishes to dish washer.

        Keyword Arguments:
        numDishes       -- number of dishes to be added.

        """
        self.dishwasherDishCount+=numDishes
        # if(self.getDishwasherDishCount()+numDishes<=self.DISHWASHERCAP):
        #     self.dishwasherDishCount+=numDishes
        # else:
        #     print("Too many dishes. Must add less")

    

    #-------------------------------------------------------------
    #   COFFEE MAKER
    #-------------------------------------------------------------

    def turnOnCoffeeMaker(self,frame,db):
        """Turns on the coffee maker."""
        self.coffeemaker.actuators[0].turnOn()
        frame.coffeeMakerStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffCoffeeMaker(self,frame,db):
        """Turns off the coffee maker."""
        self.coffeemaker.actuators[0].turnOff()
        frame.coffeeMakerStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

    def getCoffeeMakerState(self):
        """Returns the coffeemaker's state (on/off)."""
        return self.coffeemaker.actuators[0].getState()
    
    def setCoffeeMakerFlow(self, flowRate):
        """Sets the flow rate of the coffee maker.

        Keyword Arguments:
        flowRate        -- the flow rate of the coffee maker as a percent of its maximum flow.

        """
        self.coffeemaker.sensors[1].setFlowRatePct(flowRate)
    
    def getCoffeMakerFlow(self):
        """Returns the coffee maker's flow rate."""
        return self.coffeemaker.sensors[1].getFlowRatePct()

    def setCoffeeMakerTemp(self, temp):
        """Sets the coffe maker's temp.

        Keyword Arguments:
        temp        -- the temperature in degrees F.

        """
        self.coffeemaker.sensors[0].setTemp(temp)

    def getCoffeeMakerTemp(self):
        """Returns the coffee maker's temp."""
        return self.coffeemaker.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   TOASTER
    #-------------------------------------------------------------

    def turnOnToaster(self, frame,db):
        """Turns on the toaster."""
        self.toaster.actuators[0].turnOn()
        frame.toasterStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffToaster(self, frame,db):
        """Turns off the toaster."""
        self.toaster.actuators[0].turnOff()
        frame.toasterStateDisplayLabel.config(text="Off")
        frame.update()

    def getToasterState(self):
        """Returns the state of the coffee maker (on/off)."""
        return self.toaster.actuators[0].getState()

    def setToasterTemp(self, temp):
        """Sets the coffee maker's temp.

        Keyword Arguments:
        temp        -- the temperature in degrees F.

        """
        self.toaster.sensors[0].setTemp(temp)

    def getToasterTemp(self):
        """Returns the coffee maker's temp."""
        return self.toaster.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   GARBAGE DISPOSAL
    #-------------------------------------------------------------

    def turnOnGarbageDisposal(self,frame,db):
        """Turns on the garbage disposal."""
        self.garbagedisposal.actuators[0].turnOn()
        frame.garbageDisposalStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffGarbageDisposal(self,frame,db):
        """Turns off the garbage disposal."""
        self.garbagedisposal.actuators[0].turnOff()
        frame.garbageDisposalStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()


    def getGarbageDisposalState(self):
        """Returns the garbage disposal's state (on/off)."""
        return self.garbagedisposal.actuators[0].getState()

    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    def turnOnLights(self,frame,db):
        """Turns on the lights."""
        self.lights.actuators[0].turnOn()
        frame.kitchenLightsStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()
    
    def turnOffLights(self,frame,db):
        """Turns off the lights."""
        self.lights.actuators[0].turnOff()
        self.setLightBrightness(frame,0,db)
        frame.kitchenLightsStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()
    
    def getLightsState(self):
        """Returns the light's state (on/off)."""
        return self.lights.actuators[0].getState()

    def setLightBrightness(self,frame, bright,db):
        """Sets the brightness of the lights.

        Keyword Arguments:
        bright        -- the brigthness of the lights as a percent of its maximum brightness.

        """        
        self.lights.sensors[0].setBrightPct(bright)
        if bright!=0:
            self.turnOnLights(frame,db)
        frame.kitchenLightsBrightValueDisplayLabel.config(text=str(bright)+"%")
        frame.update()
        db.commit()



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
    #   DOORS
    #-------------------------------------------------------------
  
    #   NO DOORS
  
    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    #   NO WINDOWS
    
    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #AC
    def turnOnAC(self,frame,db):
        """Turns on the AC."""
        self.aircon.actuators[0].turnOn()
        frame.aCStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffAC(self,frame,db):
        """Turns off the AC."""
        self.aircon.actuators[0].turnOff()
        frame.aCStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

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
    def turnOnHeat(self,frame,db):
        """Turns on the heat."""
        self.heat.actuators[0].turnOn()
        frame.heatStateDisplayLabel.config(text="On")
        frame.update()
        db.commit()

    def turnOffHeat(self,frame,db):
        """Turns off the heat."""
        self.heat.actuators[0].turnOff()
        frame.heatStateDisplayLabel.config(text="Off")
        frame.update()
        db.commit()

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
    #   SMOKE DETECTOR
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

# #     # oven = device("Oven",cursor)

# #     # tempS = tempSensor("TS1","Oven",cursor)

# #     # oven.sensors.append(tempS)

# #     # kitchen = room("kitchen",cursor)

# #     # kitchen.devices.append(oven)
# #     # print(kitchen.devices[0].getName())
# #     kitchen1 = kitchen("Kitchen", cursor)
# #     print(kitchen1.oven.actuators[0].getState())
# #     kitchen1.turnOnOven()
# #     print(kitchen1.oven.actuators[0].getState())
# #     kitchen1.turnOffOven()
# #     print(kitchen1.oven.actuators[0].getState())
# #     print("FRIDGE")
# #     print(kitchen1.getFridgeDoorState())
# #     kitchen1.openFridgeDoor()
# #     print(kitchen1.getFridgeDoorState())
# #     kitchen1.closeFridgeDoor()
# #     print(kitchen1.getFridgeDoorState())

#     kT = kitchen("kitchen", cursor)
#     #   Testing all elements of the kitchen

#     print("------------------------------------------")
#     print("TESTING OVEN")
#     print(kT.getOvenState())
#     kT.turnOnOven()
#     print(kT.getOvenState())
#     kT.turnOffOven()
#     print(kT.getOvenState())
#     print(kT.getOvenTemp())
#     kT.setOvenTemp(7865)
#     print(kT.getOvenTemp())
#     kT.setOvenTemp(0)
#     kT.updateOvenTemp()
#     print(kT.getOvenTemp())
#     print("------------------------------------------")
#     print("TESTING FRIDGE")
#     print(kT.getFridgeState())
#     kT.turnOnFridge()
#     print(kT.getFridgeState())
#     kT.turnOffFridge()
#     print(kT.getFridgeState())
#     print(kT.getFridgeDoorState())
#     kT.openFridgeDoor()
#     print(kT.getFridgeDoorState())
#     kT.closeFridgeDoor()
#     print(kT.getFridgeDoorState())
#     print("------------------------------------------")
#     print("TESTING STOVE")
#     for i in range(4):
#         print("Testing burner number #"+str(i+1))
#         print(kT.getStoveBurnerState(i))
#         kT.turnOnStoveBurner(i)
#         print(kT.getStoveBurnerState(i))
#         kT.turnOffStoveBurner(i)
#         print(kT.getStoveBurnerState(i))
#         print(kT.getStoveBurnerTemp(i))
#         kT.setStoveBurnerTemp(i,8746)
#         print(kT.getStoveBurnerTemp(i))
#         kT.setStoveBurnerTemp(i,0)
#         kT.updateStoveBurnerTemp(i)
#         print(kT.getStoveBurnerTemp(i))
#     print("------------------------------------------")
#     print("TESTING KITCHEN SINK")
#     print(kT.getSinkState())
#     kT.turnOnSink()
#     print(kT.getSinkState())
#     kT.turnOffSink()
#     print(kT.getSinkState())
#     print(kT.getSinkFlow())
#     kT.setSinkFlow(.5)
#     print(kT.getSinkFlow())
#     print("------------------------------------------")
#     print("TESTING PANTRY SINK")
#     print(kT.getPantrySinkState())
#     kT.turnOnPantrySink()
#     print(kT.getPantrySinkState())
#     kT.turnOffPantrySink()
#     print(kT.getPantrySinkState())
#     print(kT.getPantrySinkFlow())
#     kT.setPantrySinkFlow(.5)
#     print(kT.getPantrySinkFlow())
#     print("------------------------------------------")
#     print("TESTING MICROWAVE")
#     print(kT.getMicrowaveState())
#     kT.turnOnMicrowave()
#     print(kT.getMicrowaveState())
#     kT.turnOffMicrowave()
#     print(kT.getMicrowaveState())
#     print(kT.getMicrowaveTemp())
#     kT.setMicrowaveTemp(192874)
#     print(kT.getMicrowaveTemp())
#     print("------------------------------------------")
#     print("TESTING DISHWASHER")
#     print(kT.getDishwasherState())
#     kT.turnOnDishwasher()
#     print(kT.getDishwasherState())
#     kT.turnOffDishwaser()
#     print(kT.getDishwasherState())
#     print(kT.getDishwasherFlow())
#     kT.setDishwasherFlow(.9827139)
#     print(kT.getDishwasherFlow())
#     print("------------------------------------------")
#     print("TESTING COFFEE MAKER")
#     print(kT.getCoffeeMakerState())
#     kT.turnOnCoffeeMaker()
#     print(kT.getCoffeeMakerState())
#     kT.turnOffCofeeMaker()
#     print(kT.getCoffeeMakerState())
#     print(kT.getCoffeMakerFlow())
#     kT.setCoffeeMakerFlow(.213)
#     print(kT.getCoffeMakerFlow())
#     print(kT.getCoffeeMakerTemp())
#     kT.setCoffeeMakerTemp(18247)
#     print(kT.getCoffeeMakerTemp())
#     print("------------------------------------------")
#     print("TESTING TOASTER")
#     print(kT.getToasterState())
#     kT.turnOnToaster()
#     print(kT.getToasterState())
#     kT.turnOffToaster()
#     print(kT.getToasterState())
#     print(kT.getToasterTemp())
#     kT.setToasterTemp(1029)
#     print(kT.getToasterTemp())
#     print("------------------------------------------")
#     print("TESTING GARBAGE DISPOSAL")
#     print(kT.getGarbageDisposalState())
#     kT.turnOnGarbageDisposal()
#     print(kT.getGarbageDisposalState())
#     kT.turnOffGarbageDisposal()
#     print(kT.getGarbageDisposalState())
#     print("------------------------------------------")
#     print("TESTING LIGHTS")
#     print(kT.getLightsState())
#     kT.turnOnLights()
#     print(kT.getLightsState())
#     kT.turnOffLights()
#     print(kT.getLightsState())
#     print(kT.getLightBrightness())
#     kT.setLightBrightness(.129837)
#     print(kT.getLightBrightness())
#     print(kT.getLightsMotion())
#     kT.setLightsMotion(1)
#     print(kT.getLightsMotion())
#     print("------------------------------------------")
#     print("TESTING AC/HEAT")
#     print(kT.getACState())
#     kT.turnOnAC()
#     print(kT.getACState())
#     kT.turnOffAC()
#     print(kT.getACState())
#     print(kT.getACTemp())
#     kT.setACTemp(1290470)
#     print(kT.getACTemp())
#     print(kT.getHeatState())
#     kT.turnOnHeat()
#     print(kT.getHeatState())
#     kT.turnOffHeat()
#     print(kT.getHeatState())
#     print(kT.getHeatTemp())
#     kT.setHeatTemp(9182791823719283)
#     print(kT.getHeatTemp())
#     print("------------------------------------------")
#     print("TESTING SMOKE DETECTOR")
#     print(kT.getSmokeDetectorState())
#     kT.turnOnSmokeDetector()
#     print(kT.getSmokeDetectorState())
#     kT.turnOffSmokeDetector()
#     print(kT.getSmokeDetectorState())
#     print(kT.getSmokeState())
#     kT.setSmokeState(1)
#     print(kT.getSmokeState())


#     db.commit()
#     db.close()
# main()