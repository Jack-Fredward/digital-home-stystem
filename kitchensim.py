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
        kitchen.turnOffOven()
    else:
        print("Oven already on. Should never be here.")


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
    print("TESTING OVEN SIM")
    # ovenTemp = eval(input("Enter the temp you wise to set the oven to: "))
    # kitchen1.turnOnOven()
    # simOvenTemp(kitchen1, ovenTemp)
    print("------------------------------------------")
    print("TESTING AC/HEAT SIM")
    print(kitchen1.getACTemp())
    print(kitchen1.getHeatTemp())
    print(kitchen1.getTemp())
    simACHeat(kitchen1,68)
    print('\n\n')
    print(kitchen1.getACTemp())
    print(kitchen1.getHeatTemp())
    print(kitchen1.getTemp())
    print('\n\n')
    simACHeat(kitchen1,72)
    print('\n\n')
    print(kitchen1.getACTemp())
    print(kitchen1.getHeatTemp())
    print(kitchen1.getTemp())
    simACHeat(kitchen1, 72)

    






    db.commit()
    db.close()
main()