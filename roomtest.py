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

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #-------------------------------------------------------------
        #   OVEN
        #-------------------------------------------------------------

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

        self.stove = device("Stove",dbCursor)
        for i in range(4):
            self.stove.sensors.append(tempSensor("STS"+str(i+1),"Stove",dbCursor))
            self.stove.actuators.append(actuator("Burner"+str(i+1)+" Actuator","Stove",dbCursor))

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   MICROWAVE
        #-------------------------------------------------------------


        #-------------------------------------------------------------
        #   DISH WASHER
        #-------------------------------------------------------------


        #-------------------------------------------------------------
        #   COFFEE MAKER
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   TOASTER
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   GARBAGE DISPOSAL
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   LIGHTS
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   DOORS
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------




    
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

    #-------------------------------------------------------------
    #   FRIDGE
    #-------------------------------------------------------------

    def openFridgeDoor(self):
        self.fridge.sensors[1].updateOpen()

    def closeFridgeDoor(self):
        self.fridge.sensors[1].updateClosed()

    def getFridgeDoorState(self):
        return self.fridge.sensors[1].getState()
    
    #-------------------------------------------------------------
    #   STOVE
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   MICROWAVE
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DISH WASHER
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   COFFEE MAKER
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   TOASTER
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   GARBAGE DISPOSAL
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DOORS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   CAMERAS
    #-------------------------------------------------------------

        

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