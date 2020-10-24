import pymysql
from kitchen import *
import datetime
import time

def simOvenTemp(kitchen, temp):

    if (kitchen.getOvenState()!=1):
        secondsElapsed = 0
        kitchen.turnOnOven()
        time.sleep(1)
        secondsElapsed = secondsElapsed +1
        kitchen.updateOvenTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getOvenTemp())
        while(kitchen.getOvenTemp()<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed +1
            kitchen.updateOvenTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getOvenTemp())
        # kitchen.turnOffOven()
    else:
        print("Oven already on. Should never be here.")

def simStoveTemp(kitchen,temp,burnerNum):
    if (kitchen.getStoveBurnerState(burnerNum)!=1):
        secondsElapsed = 0
        kitchen.turnOnStoveBurner(burnerNum)
        time.sleep(1)
        secondsElapsed = secondsElapsed +1
        kitchen.updateStoveBurnerTemp(burnerNum)
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getStoveBurnerTemp(burnerNum))
        while(kitchen.getStoveBurnerTemp(burnerNum)<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed +1
            kitchen.updateStoveBurnerTemp(burnerNum)
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getStoveBurnerTemp(burnerNum))
        # kitchen.turnOffStoveBurner(burnerNum)
    else:
        print("Stove Burner #"+str(burnerNum)+" already on. Should never be here.")


def simMicrowave(kitchen, microTime, powerlevel):
    #microTime is the microwave cook time   
    MICROWATTS = 900 #power of the microwave
    temp = (powerlevel/10)*MICROWATTS
    kitchen.turnOnMicrowave()
    kitchen.setMicrowaveTemp(temp)
    while microTime > 0:
        microTime = microTime - 1
        time.sleep(1)
        print("Time Left: "+str(microTime)+" at powerlevel: "+str(powerlevel)+" wattage: "+str(temp))
    print("Beep Beep Beep")

def simDishwasher(kitchen):
    numDishes = eval(input("Please enter the number of dishes you would like to add: "))
    kitchen.addDishToDishwasher(numDishes)
    print(kitchen.getDishwasherDishCount())
    while(kitchen.getDishwasherDishCount()<kitchen.getDishwasherCap()):
        numDishes = eval(input("Please enter the number of dishes you would like to add: "))
        kitchen.addDishToDishwasher(numDishes)
        print(kitchen.getDishwasherDishCount())
    print("Running Dishwasher now...")
    
def simCoffeMaker(kitchen,cupSize):
    kitchen.turnOnCoffeeMaker()
    kitchen.setCoffeeMakerTemp(200) #the average optimal temp for making coffee
    print("Heating Water For Coffee Please Wait")
    time.sleep(3)
    #cup size options small medium large
    if(cupSize == 1):
        kitchen.setCoffeeMakerFlow(.33)
        print("Dispensing Coffee Now for a Small Cup")
    elif(cupSize ==2):
        kitchen.setCoffeeMakerFlow(.66)
        print("Dispensing Coffee Now for a Medium Cup")
    else:
        kitchen.setCoffeeMakerFlow(1)
        print("Dispensing Coffee Now for a Large Cup")
    kitchen.turnOffCofeeMaker()
    kitchen.setCoffeeMakerTemp(0)
    print("Shutting Off: Enjoy your coffee")
        
def simToaster(kitchen,tempSetting):
    TOASTERTEMP = 1112 #degrees F
    TOASTERTIMEFACTOR = 2 #factor of time in seconds for each tempSetting( tempSetting 1 = 2 seconds, 2 = 4 seconds, etc)
    kitchen.turnOnToaster()
    kitchen.setToasterTemp(TOASTERTEMP)
    print("Cooking the toast for "+str(tempSetting*TOASTERTIMEFACTOR)+" seconds")
    secondsElapsed = 0
    time.sleep(1)
    secondsElapsed+=1
    print("Toasting. Time left: "+str(tempSetting*TOASTERTIMEFACTOR-secondsElapsed)+" seconds")
    while(secondsElapsed<tempSetting*TOASTERTIMEFACTOR-1):
        time.sleep(1)
        secondsElapsed+=1
        print("Toasting. Time left: "+str(tempSetting*TOASTERTIMEFACTOR-secondsElapsed)+" seconds")
    time.sleep(1)
    print("Pop! Toast is done")
    kitchen.turnOffToaster()
    kitchen.setToasterTemp(0)

def simLights(kitchen):
    print("Person enters room and turns on lights")
    kitchen.turnOnLights()
    kitchen.setLightBrightness(100)
    kitchen.setLightsMotion(1)
    time.sleep(1)
    print("Person leaves room")
    kitchen.setLightsMotion(0)
    secondsElapsed = 0
    print("Light auto turn off timer: "+str(5-secondsElapsed))
    while(secondsElapsed<5):
        time.sleep(1)
        secondsElapsed+=1
        print("Light auto turn off timer: "+str(5-secondsElapsed))
    kitchen.setLightBrightness(0)
    kitchen.turnOffLights()
    print("Turning lights off...")

def simACHeat(kitchen, temp):
    currTemp = kitchen.getTemp()
    if temp < currTemp:
        secondsElapsed = 0
        kitchen.turnOnAC()
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        kitchen.updateACTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
        while(kitchen.getTemp()>temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            kitchen.updateACTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
        kitchen.turnOffAC()
    elif temp > currTemp:
        secondsElapsed = 0
        kitchen.turnOnHeat()
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        kitchen.updateHeatTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
        while(kitchen.getTemp()<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            kitchen.updateHeatTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",kitchen.getTemp())
        kitchen.turnOffHeat()
    else:
        print("The Kitchen currently your requested temp")

def main():
    # Open database connection
    db = pymysql.connect("localhost","jp","Database","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM TempSensors")
    cursor.execute("DELETE FROM OpenCloseSensors")
    cursor.execute("DELETE FROM MotionSensors")
    cursor.execute("DELETE FROM LiquidFlowSensors")
    cursor.execute("DELETE FROM BrightnessSensor")
    cursor.execute("DELETE FROM Actuators")
    cursor.execute("DELETE FROM Devices")

    kitchen1 = kitchen("Kitchen", cursor)
    # print(kitchen1.oven.actuators[0].getState())
    # kitchen1.turnOnOven()
    # print(kitchen1.getOvenTemp())
    # print(kitchen1.oven.actuators[0].getState())
    # kitchen1.turnOffOven()
    # print(kitchen1.oven.actuators[0].getState())
    # print("------------------------------------------")
    # print("TESTING OVEN SIM")
    # ovenTemp = eval(input("Enter the temp you wise to set the oven to: "))
    # kitchen1.turnOnOven()
    # simOvenTemp(kitchen1, ovenTemp)
    # print("------------------------------------------")
    # print("TESTING AC/HEAT SIM")
    # print(kitchen1.getACTemp())
    # print(kitchen1.getHeatTemp())
    # print(kitchen1.getTemp())
    # simACHeat(kitchen1,68)
    # print('\n\n')
    # print(kitchen1.getACTemp())
    # print(kitchen1.getHeatTemp())
    # print(kitchen1.getTemp())
    # print('\n\n')
    # simACHeat(kitchen1,72)
    # print('\n\n')
    # print(kitchen1.getACTemp())
    # print(kitchen1.getHeatTemp())
    # print(kitchen1.getTemp())
    # simACHeat(kitchen1, 72)
    # print("------------------------------------------")
    # print("TESTING Stove SIM")
    # simStoveTemp(kitchen1, 100, 0)
    # print("------------------------------------------")
    # print("TESTING Microwave SIM")
    # simMicrowave(kitchen1,5, 8)
    # print("------------------------------------------")
    # print("TESTING DISHWASHER SIM")
    # simDishwasher(kitchen1)
    # print("------------------------------------------")
    # print("TESTING COFFEE MAKER SIM")
    # simCoffeMaker(kitchen1,1)
    # simCoffeMaker(kitchen1,2)
    # simCoffeMaker(kitchen1,3)
    # print("------------------------------------------")
    # print("TESTING TOASTER SIM")
    # simToaster(kitchen1, 2)
    print("------------------------------------------")
    print("TESTING LIGHT SIM")
    simLights(kitchen1)

    db.commit()
    db.close()
main()