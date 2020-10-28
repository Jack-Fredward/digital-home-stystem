# commomsim.py
import datetime
import time
from kitchen import *

def simACHeat(room, temp):
    """Simulates the setting of a desired temperature and the AC/Heat system making a room that temperature.

    Keyword Arguments:
    room     -- is the room object that this simulation pertains to, the room.
    temp        -- the temperature in degrees F.

    """
    currTemp = room.getTemp()
    if temp < currTemp:
        secondsElapsed = 0
        room.turnOnAC()
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        room.updateACTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",room.getTemp())
        while(room.getTemp()>temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            room.updateACTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",room.getTemp())
        room.turnOffAC()
    elif temp > currTemp:
        secondsElapsed = 0
        room.turnOnHeat()
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        room.updateHeatTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",room.getTemp())
        while(room.getTemp()<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            room.updateHeatTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",room.getTemp())
        room.turnOffHeat()
    else:
        print("The "+str(room.name)+" currently your requested temp")


def simLights(room):
    """Simulating someone entering and leaving a room.

    Keyword Arguments:
    room     -- is the room object that this simulation pertains to, the room.

    """
    print("Person enters the "+ str(room.name)+" and turns on lights")
    room.turnOnLights()
    room.setLightBrightness(100)
    room.setLightsMotion(1)
    time.sleep(1)
    print("Person leaves the "+str(room.name))
    room.setLightsMotion(0)
    secondsElapsed = 0
    print("Light auto turn off timer: "+str(5-secondsElapsed))
    while(secondsElapsed<4):
        time.sleep(1)
        secondsElapsed+=1
        print("Light auto turn off timer: "+str(5-secondsElapsed))
    room.setLightBrightness(0)
    room.turnOffLights()
    print("Turning lights off...")


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

    simACHeat(kitchen1, 70)
    simLights(kitchen1)


    db.commit()
    db.close()

main()