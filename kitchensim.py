import pymysql
from kitchen import *
import datetime
import time
import tkinter as tk

def simOvenTemp(db, frame, kitchen, temp):
    """Simulates setting a desired temp for the oven to be at and the oven heating up to the desired temp.

    Keyword arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.
    temp        -- the temperature in degrees F.

    """

    if (temp > 0):
        secondsElapsed = 0
        if(kitchen.getOvenState()!=1):
            kitchen.turnOnOven(frame)
        kitchen.setOvenTemp(0)
        time.sleep(1)
        secondsElapsed = secondsElapsed +1
        kitchen.updateOvenTemp()
        # frame.tempDisplayLabel.config(text = "Seconds Elapsed: "+str(secondsElapsed)+ " Temperature(F): "+str(kitchen.getOvenTemp()))
        frame.tempDisplayLabel.config(text = str(kitchen.getOvenTemp())+"*F")
        frame.update()
        # print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getOvenTemp())
        while(kitchen.getOvenTemp()<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed +1
            kitchen.updateOvenTemp()
            # frame.tempDisplayLabel.config(text = "Seconds Elapsed: "+str(secondsElapsed)+ " Temperature(F): "+str(kitchen.getOvenTemp()))
            frame.tempDisplayLabel.config(text = str(kitchen.getOvenTemp())+"*F")
            frame.update()
            # print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getOvenTemp())
        kitchen.turnOffOven(frame)
        # kitchen.setOvenTemp(0)
        db.commit()

    # else:
    #     print("Oven already on. Or entered an invalid temp (0) Should never be here.")

def simStoveTemp(db,frame,kitchen,temp,burnerNum):
    """Simulates setting a desired temp to a stove burner and the stove burner heating up to it.

    Keyword Arguments:
        kitchen     -- is the room object that this simulation pertains to, the kitchen.
        temp            -- the temp in degrees F.
        burnerNum       -- the burner number of which burner to use.
        
        """
    if (temp>0):
        secondsElapsed = 0
        kitchen.setStoveBurnerTemp(burnerNum,0)
        if(kitchen.getStoveBurnerState(burnerNum)!=1):
            kitchen.turnOnStoveBurner(frame,burnerNum,db)
        time.sleep(1)
        secondsElapsed = secondsElapsed +1
        kitchen.updateStoveBurnerTemp(burnerNum)
        frame.burnerTempDisplayLabel[burnerNum].config(text = str(kitchen.getStoveBurnerTemp(burnerNum))+"*F")
        frame.update()
        #print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getStoveBurnerTemp(burnerNum))
        while(kitchen.getStoveBurnerTemp(burnerNum)<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed +1
            kitchen.updateStoveBurnerTemp(burnerNum)
            frame.burnerTempDisplayLabel[burnerNum].config(text = str(kitchen.getStoveBurnerTemp(burnerNum))+"*F")
            frame.update()
            #print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getStoveBurnerTemp(burnerNum))
        kitchen.turnOffStoveBurner(frame,burnerNum,db)
        db.commit()
    #else:
        #print("Stove Burner #"+str(burnerNum)+" already on. Should never be here.")


def simMicrowave(db, frame,kitchen, microTime, powerlevel):
    """Simulates the behavior of setting a cook time and temp to a microwave.

    Keyword Arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.
    microTime   -- the time in seconds that the microwave will cook for.
    powerlevel  -- the power level of the microwave.

    """
    #microTime is the microwave cook time   
    MICROWATTS = 900 #power of the microwave
    powerlevel = int(powerlevel)
    microTime = int(microTime)
    temp = (powerlevel/10)*MICROWATTS
    kitchen.turnOnMicrowave(frame,db)
    kitchen.setMicrowaveTemp(temp)
    frame.microwaveCookTimeDisplay.config(text = "Time Remaining: "+str(microTime))
    frame.update()
    while microTime > 0:
        microTime = microTime - 1
        time.sleep(1)
        frame.microwaveCookTimeDisplay.config(text = "Time Remaining: "+str(microTime))
        frame.update()
        #print("Time Left: "+str(microTime)+" at powerlevel: "+str(powerlevel)+" wattage: "+str(temp))
    #print("Beep Beep Beep")
    kitchen.turnOffMicrowave(frame,db)
    db.commit()

def simDishwasher(kitchen,frame,dishes,db):
    """Simulating loading the dishwasher.

    Keyword Arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.

    """
    kitchen.addDishToDishwasher(dishes)

    if dishes <=20:
        kitchen.setDishwasherFlow(.33)
        kitchen.turnOnDishwasher(frame,db)
        frame.dishWasherFlowLabel.config(text="Flow Rate: 33%")
        frame.update()
        db.commit()
        time.sleep(3)
    elif dishes <=40:
        kitchen.setDishwasherFlow(.66)
        kitchen.turnOnDishwasher(frame,db)
        frame.dishWasherFlowLabel.config(text="Flow Rate: 66%")
        frame.update()
        db.commit()
        time.sleep(6)
    else:
        kitchen.setDishwasherFlow(1)
        kitchen.turnOnDishwasher(frame,db)
        frame.dishWasherFlowLabel.config(text="Flow Rate: 100%")
        frame.update()
        time.sleep(9)
    
    kitchen.setDishwasherFlow(0)
    kitchen.turnOffDishwasher(frame,db)
    frame.dishWasherFlowLabel.config(text="Flow Rate: 0%")
    frame.update()



    
    # numDishes = eval(input("Please enter the number of dishes you would like to add(max capcity"+str(kitchen.DISHWASHERCAP)+ "): "))
    # kitchen.addDishToDishwasher(numDishes)
    # print(kitchen.getDishwasherDishCount())
    # while(kitchen.getDishwasherDishCount()<kitchen.getDishwasherCap()):
    #     numDishes = eval(input("Please enter the number of dishes you would like to add: "))
    #     kitchen.addDishToDishwasher(numDishes)
    #     print(kitchen.getDishwasherDishCount())
    # print("Running Dishwasher now...")
    
def simCoffeeMaker(db, frame, kitchen,cupSize):
    """Simulating the coffee maker's behavior.

    Keyword Arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.
    cupSize     -- cup size to make where 1 is a small cup, 2 is a medium cup 3 is a large cup.

    """
    kitchen.turnOnCoffeeMaker(frame,db)
    # kitchen.setCoffeeMakerTemp(200) #the average optimal temp for making coffee
    #print("Heating Water For Coffee Please Wait")
    
    temp = 0
    for i in range(5):
        frame.coffeeMakerTempLabel.config(text ="Temp: "+str(temp)+" *F")
        frame.update()
        temp+=50
        time.sleep(1)
    kitchen.setCoffeeMakerTemp(temp) #the average optimal temp for making coffee
    db.commit()
    #cup size options small medium large
    if(cupSize == 1):
        kitchen.setCoffeeMakerFlow(.33)
        db.commit()
        frame.coffeeMakerFlowLabel.config(text = "Flow Rate: 33%")
        frame.update()
        #print("Dispensing Coffee Now for a Small Cup")
        time.sleep(3)
    elif(cupSize ==2):
        kitchen.setCoffeeMakerFlow(.66)
        db.commit()
        frame.coffeeMakerFlowLabel.config(text = "Flow Rate: 66%")
        frame.update()
        #print("Dispensing Coffee Now for a Medium Cup")
        time.sleep(5)
    else:
        kitchen.setCoffeeMakerFlow(1)
        db.commit()
        frame.coffeeMakerFlowLabel.config(text = "Flow Rate: 100%")
        frame.update()
        #print("Dispensing Coffee Now for a Large Cup")
        time.sleep(8)
    kitchen.turnOffCoffeeMaker(frame,db)
    temp = 0
    kitchen.setCoffeeMakerTemp(temp)
    kitchen.setCoffeeMakerFlow(0)
    db.commit()
    frame.coffeeMakerTempLabel.config(text ="Temp: "+str(temp)+" *F")
    frame.coffeeMakerFlowLabel.config(text = "Flow Rate: 0%")
    frame.update()
    #print("Shutting Off: Enjoy your coffee")
        
def simToaster(db, frame, kitchen,tempSetting):
    """Simulating a toasters behavior.

    Keyword Arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.
    tempSetting -- the temp setting from 1-10 that the toaster will cook for.

    """
    TOASTERTEMP = 1112 #degrees F
    TOASTERTIMEFACTOR = 2 #factor of time in seconds for each tempSetting( tempSetting 1 = 2 seconds, 2 = 4 seconds, etc)
    kitchen.turnOnToaster(frame,db)
    kitchen.setToasterTemp(TOASTERTEMP)
    db.commit()
    print("Cooking the toast for "+str(tempSetting*TOASTERTIMEFACTOR)+" seconds")
    secondsElapsed = 0
    frame.toasterToastTimeDisplay.config(text = "Time Remaining: "+str())
    time.sleep(1)
    secondsElapsed+=1 #REDO THE COUNTING OF TIME IN THIS FUNCTION
    print("Toasting. Time left: "+str(tempSetting*TOASTERTIMEFACTOR-secondsElapsed)+" seconds")
    while(secondsElapsed<tempSetting*TOASTERTIMEFACTOR-1):
        time.sleep(1)
        secondsElapsed+=1
        print("Toasting. Time left: "+str(tempSetting*TOASTERTIMEFACTOR-secondsElapsed)+" seconds")
    time.sleep(1)
    print("Pop! Toast is done")
    kitchen.turnOffToaster(frame,db)
    kitchen.setToasterTemp(0)
    db.commit()

def simLights(kitchen):
    """Simulating someone entering and leaving the kitchen.

    Keyword Arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.

    """
    print("Person enters room and turns on lights")
    kitchen.turnOnLights()
    kitchen.setLightBrightness(100)
    kitchen.setLightsMotion(1)
    time.sleep(1)
    print("Person leaves room")
    kitchen.setLightsMotion(0)
    secondsElapsed = 0
    print("Light auto turn off timer: "+str(5-secondsElapsed))
    while(secondsElapsed<4):
        time.sleep(1)
        secondsElapsed+=1
        print("Light auto turn off timer: "+str(5-secondsElapsed))
    kitchen.setLightBrightness(0)
    kitchen.turnOffLights()
    print("Turning lights off...")

def simACHeat(db,frame,kitchen, temp):
    """Simulates the setting of a desired temperature and the AC/Heat system making the kitchen that temperature.

    Keyword Arguments:
    kitchen     -- is the room object that this simulation pertains to, the kitchen.
    temp        -- the temperature in degrees F.

    """
    currTemp = kitchen.getTemp()
    if temp < currTemp:
        secondsElapsed = 0
        kitchen.turnOnAC(frame,db)
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        kitchen.updateACTemp()
        # print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
        frame.tempDisplayLabel.config(text = str(kitchen.getACTemp())+"*F")
        frame.update()
        while(kitchen.getTemp()>temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            kitchen.updateACTemp()
            #print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
            frame.tempDisplayLabel.config(text = str(kitchen.getACTemp())+"*F")
            frame.update()
        kitchen.turnOffAC(frame,db)
        db.commit()
    elif temp > currTemp:
        secondsElapsed = 0
        kitchen.turnOnHeat(frame,db)
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        kitchen.updateHeatTemp()
        #print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
        frame.tempDisplayLabel.config(text = str(kitchen.getHeatTemp())+"*F")
        frame.update()
        while(kitchen.getTemp()<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            kitchen.updateHeatTemp()
            #print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
            frame.tempDisplayLabel.config(text = str(kitchen.getHeatTemp())+"*F")
            frame.update()
        kitchen.turnOffHeat(frame,db)
        db.commit()
    #else:
    #    print("The Kitchen currently your requested temp")

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

#     kitchen1 = kitchen("Kitchen", cursor)
#     # print(kitchen1.oven.actuators[0].getState())
#     # kitchen1.turnOnOven()
#     # print(kitchen1.getOvenTemp())
#     # print(kitchen1.oven.actuators[0].getState())
#     # kitchen1.turnOffOven()
#     # print(kitchen1.oven.actuators[0].getState())
#     print("------------------------------------------")
#     print("TESTING OVEN SIM")
#     ovenTemp = eval(input("Enter the temp you wise to set the oven to the nearest 100 degrees F: "))
#     # kitchen1.turnOnOven()
#     simOvenTemp(kitchen1, ovenTemp)
#     print("------------------------------------------")
#     print("TESTING AC/HEAT SIM")
#     print("AC temp sensor ",kitchen1.getACTemp())
#     print("Heat temp sensor ",kitchen1.getHeatTemp())
#     print("Room temp sensor ",kitchen1.getTemp())
#     # simACHeat(kitchen1,68)
#     desriedTemp = eval(input("Please enter desired temp: "))
#     simACHeat(kitchen1,desriedTemp)
#     # print('\n\n')
#     print("AC temp sensor ",kitchen1.getACTemp())
#     print("Heat temp sensor ",kitchen1.getHeatTemp())
#     print("Room temp sensor ",kitchen1.getTemp())
#     print('\n\n')
#     # simACHeat(kitchen1,72)
#     desriedTemp = eval(input("Please enter desired temp: "))
#     simACHeat(kitchen1,desriedTemp)
#     # print('\n\n')
#     print("AC temp sensor ",kitchen1.getACTemp())
#     print("Heat temp sensor ",kitchen1.getHeatTemp())
#     print("Room temp sensor ",kitchen1.getTemp())
#     simACHeat(kitchen1, 71)
#     print("AC temp sensor ",kitchen1.getACTemp())
#     print("Heat temp sensor ",kitchen1.getHeatTemp())
#     print("Room temp sensor ",kitchen1.getTemp())
#     print("------------------------------------------")
#     print("TESTING Stove SIM")
#     stoveTemp = eval(input("Please enter the desired temp for stove burner to the nearest 50 degrees F: "))
#     simStoveTemp(kitchen1, stoveTemp, 0)
#     # simStoveTemp(kitchen1, 100, 0)
#     print("------------------------------------------")
#     print("TESTING Microwave SIM")
#     microTime = eval(input("Please enter the time in seconds you would like to microwave for: "))
#     powerLevel = eval(input("Please enter the power level for the microwave from 1-10: "))
#     simMicrowave(kitchen1,microTime, powerLevel)
#     # simMicrowave(kitchen1,5, 8)
#     print("------------------------------------------")
#     print("TESTING DISHWASHER SIM")
#     simDishwasher(kitchen1)
#     print("------------------------------------------")
#     print("TESTING COFFEE MAKER SIM")
#     cupSize = eval(input("Please enter the cupSize you would like 1(sm), 2(md), 3(lg): "))
#     simCoffeMaker(kitchen1,cupSize)
#     # simCoffeMaker(kitchen1,1)
#     # simCoffeMaker(kitchen1,2)
#     # simCoffeMaker(kitchen1,3)
#     print("------------------------------------------")
#     print("TESTING TOASTER SIM")
#     dialSetting = eval(input("Please enter your desired toaster setting from 1 to 10: "))
#     simToaster(kitchen1, dialSetting)
#     print("------------------------------------------")
#     print("TESTING LIGHT SIM")
#     simLights(kitchen1)

#     db.commit()
#     db.close()
# main()