#ovensim.py

import pymysql
from kitchen import *
import datetime
import time

def simOvenTemp(kitchen, temp):
    # DELTAT = 100 #100 degrees per second
    
    
    # lut = kitchen.oven.actuators[0].getLUT()
    # now = datetime.datetime.now()
    # timeDiff = now - lut
    # # print(lut)
    # # print(now)
    # # print(timeDiff)
    # secondsElapsed = round(timeDiff.total_seconds())
    # # print(secondsElapsed)
    # oldTemp=kitchen.getOvenTemp()
    # # print(oldTemp)
    # kitchen.setOvenTemp(oldTemp+(secondsElapsed*DELTAT))
    # kitchen.updateOvenTemp()
    # print(kitchen.getOvenTemp())

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
    print("------------------------------------------")
    print("TESTING OVEN SIM")
    ovenTemp = eval(input("Enter the temp you wise to set the oven to: "))
    # kitchen1.turnOnOven()
    simOvenTemp(kitchen1, ovenTemp)




    db.commit()
    db.close()
main()