#roomtest.py

import pymysql
from device import *


# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class kitchen:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor
        self.oven = device("Oven",dbCursor)
        tempS = tempSensor("TS1","Oven",dbCursor)
        self.oven.sensors.append(tempS)
        ovenAct = actuator("Oven Actuator", "Oven",dbCursor)
        self.oven.actuators.append(ovenAct)
        self.fridge = device("Fridge",dbCursor)
        tempS2 = tempSensor("TS2","Fridge",dbCursor)
        self.fridge.sensors.append(tempS2)
        fridgeDoorSensor=openCloseSensors("Fridge Door OCS","Fridge",dbCursor)
        self.fridge.sensors.append(fridgeDoorSensor)

    def turnOnOven(self):
        self.oven.actuators[0].turnOn()

    def turnOffOven(self):
        self.oven.actuators[0].turnOff()

    def getOvenTemp(self):
        return self.oven.sensors[0].getTemp()

    def openFridgeDoor(self):
        self.fridge.sensors[1].updateOpen()

    def closeFridgeDoor(self):
        self.fridge.sensors[1].updateClosed()

    def getFridgeDoorState(self):
        return self.fridge.sensors[1].getState()
        
        

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

    # oven = device("Oven",cursor)

    # tempS = tempSensor("TS1","Oven",cursor)

    # oven.sensors.append(tempS)

    # kitchen = room("kitchen",cursor)

    # kitchen.devices.append(oven)
    # print(kitchen.devices[0].getName())
    kitchen1 = kitchen("Kitchen", cursor)
    print(kitchen1.oven.actuators[0].getState())
    kitchen1.turnOnOven()
    print(kitchen1.oven.actuators[0].getState())
    kitchen1.turnOffOven()
    print(kitchen1.oven.actuators[0].getState())
    print("FRIDGE")
    print(kitchen1.getFridgeDoorState())
    kitchen1.openFridgeDoor()
    print(kitchen1.getFridgeDoorState())
    kitchen1.closeFridgeDoor()
    print(kitchen1.getFridgeDoorState())



    db.commit()
    db.close()
main()