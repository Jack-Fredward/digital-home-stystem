# device.py

#update the get functions to query the database

import pymysql
import datetime

class device:
    def __init__(self, name, dbCursor):
        self.name = name
        dbCursor.execute("INSERT INTO Devices (D_Name) VALUES (\""+name+"\");")

    def getName(self):
        return self.name
    


class actuator:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.state = 0
        self.lut = datetime.datetime.now()
        dbCursor.execute("INSERT INTO Actuators (D_ID, State, LUT, A_Name) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), 0, \""+str(self.lut)+"\",\""+name+"\");")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getState(self):
        return self.state

    def getLUT(self):
        return self.lut

    def turnOn(self, dbCursor):
        if(self.state != 1):
            self.state=1
            self.lut=datetime.datetime.now()
            dbCursor.execute("UPDATE Actuators SET State=1, LUT=\""+str(self.lut)+"\" WHERE A_Name = \""+self.name+"\";")
        else:
            print("Device already on")
            

    def turnOff(self, dbCursor):
        if(self.state != 0):
            self.state=0
            self.lut=datetime.datetime.now()
            dbCursor.execute("UPDATE Actuators SET State=0, LUT=\""+str(self.lut)+"\" WHERE A_Name = \""+self.name+"\";")
        else:
            print("Device already off")


class brightSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.brightPct = 0
        dbCursor.execute("INSERT INTO BrightnessSensor (D_ID, BS_Name, BrightnessPct) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        self.deviceName

    def getBrightPct(self):
        return self.brightPct

    def setBrightPct(self, value, dbCursor):
        self.brightPct = value
        dbCursor.execute("UPDATE BrightnessSensor SET BrightnessPct=\""+str(value)+"\" WHERE BS_Name = \""+self.name+"\";")


class liquidFlowSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name=name
        self.deviceName=deviceName
        self.flowRatePct=0
        dbCursor.execute("INSERT INTO LiquidFlowSensors (D_ID, LFS_Name, FlowRatePct) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.name

    def getFlowRatePct(self):
        return self.flowRatePct

    def setFlowRatePct(self, value, dbCursor):
        self.flowRatePct = value
        dbCursor.execute("UPDATE LiquidFlowSensors SET FlowRatePct=\""+str(value)+"\" WHERE LFS_Name = \""+self.name+"\";")
    

class motionSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName=deviceName
        self.isMotion=0
        dbCursor.execute("INSERT INTO MotionSensors (D_ID, MS_Name, Is_Motion) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getMotion(self):
        return self.isMotion

    def updateIsMotion(self,value,dbCursor):
        dbCursor.execute("UPDATE MotionSensors SET Is_Motion=\""+str(value)+"\" WHERE MS_Name = \""+self.name+"\";")

class openCloseSensors:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.state = 0 #0 is closed
        dbCursor.execute("INSERT INTO OpenCloseSensors (D_ID, OCS_Name, State) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getState(self):
        return self.state

    def updateOpen(self, dbCursor):
        if(self.state != 1):
            self.state=1
            dbCursor.execute("UPDATE OpenCloseSensors SET State=1 WHERE OCS_Name = \""+self.name+"\";")
        else:
            print("Device already open")

    def updateClosed(self, dbCursor):
        if(self.state != 0):
            self.state=0
            dbCursor.execute("UPDATE OpenCloseSensors SET State=0 WHERE OCS_Name = \""+self.name+"\";")
        else:
            print("Device already closed")

class tempSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.temp = 0
        dbCursor.execute("INSERT INTO TempSensors (D_ID, TS_Name, Temp) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getTemp(self):
        return self.temp

    def setTemop(self, value, dbCursor):
        self.temp = value
        dbCursor.execute("UPDATE TempSensors SET Temp=\""+str(value)+"\" WHERE TS_Name = \""+self.name+"\";")

    

    



def main():
    # Open database connection
    db = pymysql.connect("localhost","jp","Database","digital_home_database" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM OpenCloseSensors")
    cursor.execute("DELETE FROM MotionSensors"
    cursor.execute("DELETE FROM LiquidFlowSensors")
    cursor.execute("DELETE FROM BrightnessSensor")
    cursor.execute("DELETE FROM Actuators")
    cursor.execute("DELETE FROM Devices")

    oven = device("Oven", cursor)
    #print(oven.getName())
    ovenActuator = actuator("OvenActuator",oven.getName(),cursor)
    ovenActuator.turnOn(cursor)
    ovenActuator.turnOff(cursor)

    light = device("light", cursor)
    lightSensor = brightSensor("brightSense1",light.getName(),cursor)
    lightSensor.setBrightPct(50,cursor)
    print(lightSensor.getBrightPct())


    cursor.execute("SELECT * FROM Devices")

    results = cursor.fetchall()

    print(results)

    cursor.execute("SELECT * FROM Actuators")

    results = cursor.fetchall()

    print(results)

    cursor.execute("SELECT * FROM BrightnessSensor")

    print(cursor.fetchall())

    db.commit()
    db.close()
main()