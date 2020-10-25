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
        
    
    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   OVEN
    #-------------------------------------------------------------

    def turnOnOven(self):
        """"Turns on the oven."""
        self.oven.actuators[0].turnOn()

    def turnOffOven(self):
        """Turns off the oven."""
        self.oven.actuators[0].turnOff()

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

    def turnOnFridge(self):
        """Turns on the fridge."""
        self.fridge.actuators[0].turnOn()

    def turnOffFridge(self):
        """Turns off the fridge."""
        self.fridge.actuators[0].turnOff()

    def getFridgeState(self):
        """Returns the fridge's state (on/off)."""
        return self.fridge.actuators[0].getState()
    
    def openFridgeDoor(self):
        """Opens the fridge door."""
        self.fridge.sensors[0].updateOpen()

    def closeFridgeDoor(self):
        """Closes the fridge door."""
        self.fridge.sensors[0].updateClosed()

    def getFridgeDoorState(self):
        """Returns the fridge door's state (open/close)."""
        return self.fridge.sensors[0].getState()
    
    #-------------------------------------------------------------
    #   STOVE
    #-------------------------------------------------------------

    def turnOnStoveBurner(self, burnerNum):
        """Turns on the Stove burner.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        self.stove.actuators[burnerNum].turnOn()

    def turnOffStoveBurner(self, burnerNum):
        """Turns off the Stove burner.

        Keyword Arguments:
        burnerNum       -- the burner number of which burner to use.

        """
        self.stove.actuators[burnerNum].turnOff()

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
    def turnOnSink(self):
        """Turns on the kitchen sink."""
        self.sink.actuators[0].turnOn()

    def turnOffSink(self):
        """Turns off the kitchen sink."""
        self.sink.actuators[0].turnOff()

    def getSinkState(self):
        """Returns the kitchen sink's state (on/off)."""
        return self.sink.actuators[0].getState()

    def setSinkFlow(self, flowRate):
        """Sets the flow rate of the kitchen sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.sink.sensors[0].setFlowRatePct(flowRate)

    def getSinkFlow(self):
        """Returns the kitchen sink's flow rate."""
        return self.sink.sensors[0].getFlowRatePct()
    
    #Pantry Sink
    def turnOnPantrySink(self):
        """Turns on the pantry sink."""
        self.pantrysink.actuators[0].turnOn()
    
    def turnOffPantrySink(self):
        """Turns off the panty sink."""
        self.pantrysink.actuators[0].turnOff()

    def getPantrySinkState(self):
        """Gets the panty sink's state (on/off)."""
        return self.pantrysink.actuators[0].getState()

    def setPantrySinkFlow(self, flowRate):
        """Sets the flow rate of the pantry sink.

        Keyword Arguments:
        flowRate        -- the flow rate of the sink as a percent of its maximum flow.

        """
        self.pantrysink.sensors[0].setFlowRatePct(flowRate)

    def getPantrySinkFlow(self):
        """Returns the pantry sink's flow rate."""
        return self.pantrysink.sensors[0].getFlowRatePct()

    #-------------------------------------------------------------
    #   MICROWAVE
    #-------------------------------------------------------------

    def turnOnMicrowave(self):
        """Turns on the microwave."""
        self.microwave.actuators[0].turnOn()

    def turnOffMicrowave(self):
        """Turns off the microwave"""
        self.microwave.actuators[0].turnOff()

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

    def turnOnDishwasher(self):
        """Turns on the dishwasher."""
        self.dishwasher.actuators[0].turnOn()

    def turnOffDishwaser(self):
        """Turns off the dishwasher."""
        self.dishwasher.actuators[0].turnOff()

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

    def getDishwasherCap(self):
        """Returns the dishwasher's max dish capacity."""
        return self.DISHWASHERCAP

    def getDishwasherDishCount(self):
        """Returns the dishwasher's dish count."""
        return self.dishwasherDishCount
    
    def addDishToDishwasher(self,numDishes):
        """Adds dishes to dish washer.

        Keyword Arguments:
        numDishes       -- number of dishes to be added.

        """
        if(self.getDishwasherDishCount()+numDishes<=self.DISHWASHERCAP):
            self.dishwasherDishCount+=numDishes
        else:
            print("Too many dishes. Must add less")

    

    #-------------------------------------------------------------
    #   COFFEE MAKER
    #-------------------------------------------------------------

    def turnOnCoffeeMaker(self):
        """Turns on the coffee maker."""
        self.coffeemaker.actuators[0].turnOn()

    def turnOffCofeeMaker(self):
        """Turns off the coffee maker."""
        self.coffeemaker.actuators[0].turnOff()

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

    def turnOnToaster(self):
        """Turns on the toaster."""
        self.toaster.actuators[0].turnOn()

    def turnOffToaster(self):
        """Turns off the toaster."""
        self.toaster.actuators[0].turnOff()

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
        self.toaster.sensors[0].getTemp()

    #-------------------------------------------------------------
    #   GARBAGE DISPOSAL
    #-------------------------------------------------------------

    def turnOnGarbageDisposal(self):
        """Turns on the garbage disposal."""
        self.garbagedisposal.actuators[0].turnOn()

    def turnOffGarbageDisposal(self):
        """Turns off the garbage disposal."""
        self.garbagedisposal.actuators[0].turnOff()

    def getGarbageDisposalState(self):
        """Returns the garbage disposal's state (on/off)."""
        return self.garbagedisposal.actuators[0].getState()

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
    def turnOnAC(self):
        """Turns on the AC."""
        self.aircon.actuators[0].turnOn()

    def turnOffAC(self):
        """Turns off the AC."""
        self.aircon.actuators[0].turnOff()

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
    def turnOnHeat(self):
        """Turns on the heat."""
        self.heat.actuators[0].turnOn()

    def turnOffHeat(self):
        """Turns off the heat."""
        self.heat.actuators[0].turnOff()

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