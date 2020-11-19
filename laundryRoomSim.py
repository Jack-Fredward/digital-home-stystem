import pymysql
from laundryRoom import *
import datetime
import time
import tkinter as tk

# def simWasher(frame, laundryRoom, temp, flowRate, db):

def simWasher(laundryRoom, loadSize, tempSet, soilLevel, frame, db):
    print("Washer Sim")
    # loadSize = int(input("Enter load size, small(1),med(2),large(3)"))
    # tempSet = int(input("Enter temp settings, cold(1),warm(2),hot(3)"))
    # soilLevel = int(input("Enter soil level, light(1), normal(2), heavy(3)"))

    if(loadSize == 1):
        laundryRoom.setWasherFlow(.33)
        frame.flowLabel.config(text = "Flow Rate: 33%")
    elif(loadSize == 2):
        laundryRoom.setWasherFlow(.66)
        frame.flowLabel.config(text = "Flow Rate: 66%")
    elif(loadSize == 3):
        laundryRoom.setWasherFlow(1)
        frame.flowLabel.config(text = "Flow Rate: 100%")
    frame.update()

    if(tempSet == 1):
        laundryRoom.setWasherTemp(70)
        frame.waterTempLabel.config(text = "Water Temp(f): 70")
    elif(tempSet == 2):
        laundryRoom.setWasherTemp(100)
        frame.waterTempLabel.config(text = "Water Temp(f): 100")
    elif(tempSet == 3):
        laundryRoom.setWasherTemp(130)
        frame.waterTempLabel.config(text = "Water Temp(f): 130")

    frame.update()

    if(soilLevel == 1):
        cycleTime = 3
    elif(soilLevel == 2):
        cycleTime = 5
    elif(soilLevel == 3):
        cycleTime = 10

    # print("Running washer with your settings")
    # print(loadSize," ",tempSet," ",soilLevel)
    frame.washerStatusLabel.config(text = "Washing")
    frame.timeLeftLabel.config(text = "Time Left: "+str(cycleTime))
    frame.update()
    for i in range(cycleTime):
        time.sleep(1)
        frame.timeLeftLabel.config(text = "Time Left: "+str(cycleTime-i-1))
        frame.update()

    frame.washerStatusLabel.config(text="Done")
    frame.waterTempLabel.config(text = "Water Temp(f): ")
    frame.flowLabel.config(text = "Flow Rate: 0%")
    frame.update()
    db.commit()
    # print("Washer Done")



def simDryer(laundryRoom,tempSet,duration,frame,db):
    if(tempSet == 1):
        laundryRoom.setDryerTemp(125)
        frame.dryerTempLabel.config(text = "Dryer Temp(f): 125")
    elif(tempSet == 2):
        laundryRoom.setWasherTemp(135)
        frame.dryerTempLabel.config(text = "Dryer Temp(f): 135")
    elif(tempSet == 3):
        laundryRoom.setWasherTemp(145)
        frame.dryerTempLabel.config(text = "Dryer Temp(f): 145")

    frame.update()

    if(duration == 1):
        cycleTime = 3
    elif(duration == 2):
        cycleTime = 5
    elif(duration == 3):
        cycleTime = 10

    # print("Running washer with your settings")
    # print(loadSize," ",tempSet," ",soilLevel)
    frame.dryerStatusLabel.config(text = "Drying")
    frame.timeLeftLabel.config(text = "Time Left: "+str(cycleTime))
    frame.update()
    for i in range(cycleTime):
        time.sleep(1)
        frame.timeLeftLabel.config(text = "Time Left: "+str(cycleTime-i-1))
        frame.update()

    frame.dryerStatusLabel.config(text="Done")
    frame.dryerTempLabel.config(text = "Water Temp(f): ")
    frame.update()
    db.commit()
    # print("Dryer Done")


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

#     lR = laundryRoom("laundry room", cursor)
#     simDryer(lR)


# main()