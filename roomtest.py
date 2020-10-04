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

    def turnOnOven(self):
        self.oven.actuators[0].turnOn()

    def turnOffOven(self):
        self.oven.actuators[0].turnOn()

    def getOvenTemp(self):
        return self.oven.sensors[0].getTemp()

        
        

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
    kitchen1.turnOnOven()
    print(kitchen1.oven.actuators[0].getState())




    db.commit()
    db.close()
main()