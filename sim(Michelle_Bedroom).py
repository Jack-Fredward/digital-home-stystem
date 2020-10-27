import pymysql
from Michelle_Bedroom import *
import datetime
import time


def simLights(Michelle_Bedroom):
    # simulights someone entering and leaving the room 
    print("Person enters room and turns on lights")
    lights.turnOnLights()
    lights.setLightBrightness(100)
    lights.setLightsMotion(1)
    time.sleep(1)
    print("Person leaves room")
    lights.setLightsMotion(0)
    secondsElapsed = 0
    print("Light auto turn off timer: "+str(5-secondsElapsed))
    while(secondsElapsed<5):
        time.sleep(1)
        secondsElapsed+=1
        print("Light auto turn off timer: "+str(5-secondsElapsed))
    lights.setLightBrightness(0)
    lights.turnOffLights()
    print("Turning lights off...")
        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------
def simACHeat(Michelle_Bedroom, temp):
#simulates the setting of a desired temperature and the AC/heat system making the reem that temp.
    currTemp = lights.getTemp()
    if temp < currTemp:
        secondsElapsed = 0
        lights.turnOnAC()
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        lights.updateACTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",lights.getTemp())
        while(lights.getTemp()>temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            lights.updateACTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",lights.getTemp())
        lights.turnOffAC()
    elif temp > currTemp:
        secondsElapsed = 0
        lights.turnOnHeat()
        time.sleep(1)
        secondsElapsed = secondsElapsed + 1
        lights.updateHeatTemp()
        print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",lights.getTemp())
        while(lights.getTemp()<temp):
            time.sleep(1)
            secondsElapsed = secondsElapsed + 1
            lights.updateHeatTemp()
            print("Seconds Elapsed: ",secondsElapsed, " ","Temperature(F): ",lights.getTemp())
        lights.turnOffHeat()
    else:
        print("The Bedroom currently your requested temp")

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