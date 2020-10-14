#laundry_room.py

import pymysql
from device import *
import datetime

# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class laundry_room:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #------------------------------------------------------------- 
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Laundry Room Lights",dbCursor)
        self.lights.actuators.append(actuator("Laundry Room Light Actuator","Laundry Room Lights",dbCursor))
        self.lights.sensors.append(brightSensor("LRLBS","Laundry Room Lights", dbCursor))
        self.lights.sensors.append(motionSensor("LRLMS","Laundry Room Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS needs finishing self.doors or self.garagedoor.append
        #-------------------------------------------------------------

        self.doors = [interiordoor, garagedoor]
        self.doors.append(device("LRinteriordoor",dbCursor))
        self.doors.actuators.append(actuator("Laundry Room Interior Door Actuator", "LRinteriordoor",dbCursor))
        self.doors.sensors.append(openCloseSensors("LRIDOCS","LRinteriordoor",dbCursor))
        self.doors.append(device("LRgaragedoor",dbCursor))
        self.doors.actuators.append(actuator("Laundry Room Garage Door Actuator", "LRgaragedoor",dbCursor))
        self.doors.sensors.append(openCloseSensors("LRGDOCS","LRgaragedoor",dbCursor))

        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        # NO WINDOWS

        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("LRATS","Air",dbCursor))
        self.air.actuators.append(actuator("Laundry Room Air Actuator","Air",dbCursor))

        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------

        self.cameras = []
        self.cameras.append(device("Laundry Room 1",dbCursor))
        self.cameras[0].actuators.append(actuator("Laundry Room Camera 1 Actuator","Laundry Room Camera 1",dbCursor))
        self.cameras[0].sensors.append(motionSensor("LRC1MS","Laundry Room Camera 1",dbCursor))

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("Sink", dbCursor)
        self.sink.actuators.append(actuator("Sink Actuator","Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("SLFS","Sink",dbCursor))

        #-------------------------------------------------------------
        #   WASHING MACHINE
        #-------------------------------------------------------------

        self.washingmachine = device("Washing Machine",dbCursor)
        self.washingmachine.actuators.append(actuator("Washing Machine Actuator", "Washing Machine", dbCursor))
        self.washingmachine.sensors.append(liquidFlowSensor("WMLFS","Washing Machine", dbCursor))

        #-------------------------------------------------------------
        #   DRYER
        #-------------------------------------------------------------

        self.dryer = device("Dryer",dbCursor)
        self.dryer.actuators.append(actuator("Dryer Actuator", "Dryer", dbCursor))
        self.dryer.sensors.append(MoistureSensor("DMS","Dryer", dbCursor))

        #-------------------------------------------------------------
        #   SMOKE ALARM
        #-------------------------------------------------------------

        self.smokealarm = device("Smoke Alarm", dbCursor)
        self.smokealarm.sensor.append(SmokeSensor("LRSS","Smoke Alarm", dbCursor))


    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   WASHING MACHINE need cycle notification
    #-------------------------------------------------------------

    def turnOnWashingMachine(self):
        self.washingmachine.actuators[0].turnOn()

    def turnOffWashingMachine(self):
        self.washingmachine.actuators.[0].turnOff()


    #-------------------------------------------------------------
    #   DRYER need cycle notification moisture sensor?
    #-------------------------------------------------------------

    def turnOnDryer(self):
        self.Dryer.actuators[0].turnOn()

    def turnOffDryer(self):
        self.Dryer.actuators[0].turnOff()
