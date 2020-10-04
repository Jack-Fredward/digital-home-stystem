# device.py

#update the get functions to query the database
#instead of having it use the name of the device could use the id by making the id be part of the object immediately upon init. Upside using id, downside work to change everything. Benefit no real difference cause name will be unique for each device,sensor anyways
#change so that both get name and get device name look it up in the database rather than storing it locally. this would entail passing the device id to the sensors rather than the device name. however we will still need to know the name at least once to get the id


import pymysql
import datetime

class device:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor
        dbCursor.execute("INSERT INTO Devices (D_Name) VALUES (\""+name+"\");")
        self.dID = self.getDID()

    def getName(self):
        return self.name

    def getDID(self):
        self.dbCursor.execute("SELECT D_ID FROM Devices WHERE D_Name = '"+self.name+"';")
        return int(self.dbCursor.fetchall()[0][0])
    


class actuator:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.dbCursor = dbCursor
        dbCursor.execute("INSERT INTO Actuators (D_ID, State, LUT, A_Name) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), 0, \""+str(datetime.datetime.now())+"\",\""+name+"\");")


    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getAID(self):
        self.dbCursor.execute("SELECT A_ID FROM Actuators WHERE A_Name = '"+self.name+"'AND D_ID = (SELECT D_ID FROM Devices WHERE D_Name=\""+self.getDeviceName()+"\");")
        return int(self.dbCursor.fetchall()[0][0])

    def getState(self):
        self.dbCursor.execute("SELECT State FROM Actuators WHERE A_ID = '"+str(self.getAID())+"';")
        return int(self.dbCursor.fetchall()[0][0])

    def getLUT(self):
        self.dbCursor.execute("SELECT LUT FROM Actuators WHERE A_ID = '"+str(self.getAID())+"';")
        return self.dbCursor.fetchall()[0][0]

    def turnOn(self):

        if(self.getState() != 1):
            self.dbCursor.execute("UPDATE Actuators SET State=1, LUT=\""+str(datetime.datetime.now())+"\" WHERE A_ID = \""+str(self.getAID())+"\";")
        else:
            print("Device already on")
            
    def turnOff(self):
        if(self.getState() != 0):
            self.dbCursor.execute("UPDATE Actuators SET State=0, LUT=\""+str(datetime.datetime.now())+"\" WHERE A_ID = \""+str(self.getAID())+"\";")
        else:
            print("Device already off")


class brightSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.dbCursor = dbCursor
        dbCursor.execute("INSERT INTO BrightnessSensor (D_ID, BS_Name, BrightnessPct) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")
      

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getBSID(self):
        self.dbCursor.execute("SELECT BS_ID FROM BrightnessSensor WHERE BS_Name = '"+self.name+"'AND D_ID = (SELECT D_ID FROM Devices WHERE D_Name=\""+self.getDeviceName()+"\");")
        return int(self.dbCursor.fetchall()[0][0])

    def getBrightPct(self):
        self.dbCursor.execute("SELECT BrightnessPct FROM BrightnessSensor WHERE BS_ID = '"+str(self.getBSID())+"';")
        return float(self.dbCursor.fetchall()[0][0])

    def setBrightPct(self, value):
        self.dbCursor.execute("UPDATE BrightnessSensor SET BrightnessPct=\""+str(value)+"\" WHERE BS_ID = \""+str(self.getBSID())+"\";")


class liquidFlowSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name=name
        self.deviceName=deviceName
        self.dbCursor=dbCursor
        dbCursor.execute("INSERT INTO LiquidFlowSensors (D_ID, LFS_Name, FlowRatePct) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getLFSID(self):
        self.dbCursor.execute("SELECT LFS_ID FROM LiquidFlowSensors WHERE LFS_Name = '"+self.name+"'AND D_ID = (SELECT D_ID FROM Devices WHERE D_Name=\""+self.getDeviceName()+"\");")
        return int(self.dbCursor.fetchall()[0][0])

    def getFlowRatePct(self):
        self.dbCursor.execute("SELECT FlowRatePct FROM LiquidFlowSensors WHERE LFS_ID = '"+str(self.getLFSID())+"';")
        return float(self.dbCursor.fetchall()[0][0])

    def setFlowRatePct(self, value):
        self.dbCursor.execute("UPDATE LiquidFlowSensors SET FlowRatePct=\""+str(value)+"\" WHERE LFS_ID = \""+str(self.getLFSID())+"\";")
    

class motionSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName=deviceName
        self.dbCursor = dbCursor
        dbCursor.execute("INSERT INTO MotionSensors (D_ID, MS_Name, Is_Motion) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getMSID(self):
        self.dbCursor.execute("SELECT MS_ID FROM MotionSensors WHERE MS_Name = '"+self.name+"'AND D_ID = (SELECT D_ID FROM Devices WHERE D_Name=\""+self.getDeviceName()+"\");")
        return int(self.dbCursor.fetchall()[0][0])

    def getMotion(self):
        self.dbCursor.execute("SELECT Is_Motion FROM MotionSensors WHERE MS_ID = '"+str(self.getMSID())+"';")
        return int(self.dbCursor.fetchall()[0][0])

    def updateIsMotion(self,value):
        self.dbCursor.execute("UPDATE MotionSensors SET Is_Motion=\""+str(value)+"\" WHERE MS_ID = \""+str(self.getMSID())+"\";")

class openCloseSensors:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.dbCursor = dbCursor
        dbCursor.execute("INSERT INTO OpenCloseSensors (D_ID, OCS_Name, State) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getOCSID(self):
        self.dbCursor.execute("SELECT OCS_ID FROM OpenCloseSensors WHERE OCS_Name = '"+self.name+"'AND D_ID = (SELECT D_ID FROM Devices WHERE D_Name=\""+self.getDeviceName()+"\");")
        return int(self.dbCursor.fetchall()[0][0])

    def getState(self):
        self.dbCursor.execute("SELECT State FROM OpenCloseSensors WHERE OCS_ID = '"+str(self.getOCSID())+"';")
        return int(self.dbCursor.fetchall()[0][0])

    def updateOpen(self):
        if(self.getState() != 1):
            self.dbCursor.execute("UPDATE OpenCloseSensors SET State=1 WHERE OCS_ID = \""+str(self.getOCSID())+"\";")
        else:
            print("Device already open")

    def updateClosed(self):
        if(self.getState() != 0):
            self.dbCursor.execute("UPDATE OpenCloseSensors SET State=0 WHERE OCS_ID = \""+str(self.getOCSID())+"\";")
        else:
            print("Device already closed")

class tempSensor:
    def __init__(self, name, deviceName, dbCursor):
        self.name = name
        self.deviceName = deviceName
        self.dbCursor = dbCursor
        dbCursor.execute("INSERT INTO TempSensors (D_ID, TS_Name, Temp) VALUES ((SELECT D_ID FROM Devices WHERE D_Name=\""+deviceName+"\"), \""+name+"\",0);")

    def getName(self):
        return self.name

    def getDeviceName(self):
        return self.deviceName

    def getTSID(self):
        self.dbCursor.execute("SELECT TS_ID FROM TempSensors WHERE TS_Name = '"+self.name+"'AND D_ID = (SELECT D_ID FROM Devices WHERE D_Name=\""+self.getDeviceName()+"\");")
        return int(self.dbCursor.fetchall()[0][0])

    def getTemp(self):
        self.dbCursor.execute("SELECT Temp FROM TempSensors WHERE TS_ID = '"+str(self.getTSID())+"';")
        return float(self.dbCursor.fetchall()[0][0])

    def setTemp(self, value):
        self.dbCursor.execute("UPDATE TempSensors SET Temp=\""+str(value)+"\" WHERE TS_ID = \""+str(self.getTSID())+"\";")

    

    



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

    oven = device("Oven", cursor)
    print(oven.getName())
    print(oven.getDID())
    print("------------------------------------------------------")

    ovenActuator = actuator("OvenActuator",oven.getName(),cursor)
    print(ovenActuator.getName())
    print(ovenActuator.getAID())
    print(ovenActuator.getDeviceName())
    print(ovenActuator.getLUT())
    print(ovenActuator.getState())
    ovenActuator.turnOn()
    print(ovenActuator.getLUT())
    print(ovenActuator.getState())
    ovenActuator.turnOff()
    print(ovenActuator.getLUT())
    print(ovenActuator.getState())
    
    print("------------------------------------------------------")
    light = device("light", cursor)
    lightSensor = brightSensor("brightSense1",light.getName(),cursor)
    print(lightSensor.getName())
    print(lightSensor.getBSID())
    print(lightSensor.getDeviceName())
    print(lightSensor.getBrightPct())
    lightSensor.setBrightPct(50)
    print(lightSensor.getBrightPct())

    print("------------------------------------------------------")
    sink = device("Sink",cursor)
    sinkSensor = liquidFlowSensor("SinkLFS1",sink.getName(),cursor)
    print(sinkSensor.getName())
    print(sinkSensor.getLFSID())
    print(sinkSensor.getDeviceName())
    print(sinkSensor.getFlowRatePct())
    sinkSensor.setFlowRatePct(50)
    print(sinkSensor.getFlowRatePct())

    print("------------------------------------------------------")
    motionDevice = device("MotionDevice",cursor)
    motSensor = motionSensor("MS1",motionDevice.getName(),cursor)
    print(motSensor.getName())
    print(motSensor.getDeviceName())
    print(motSensor.getMSID())
    print(motSensor.getMotion())
    motSensor.updateIsMotion(1)
    print(motSensor.getMotion())

    print("------------------------------------------------------")
    door = device("main door",cursor)
    doorSen = openCloseSensors("MDOC",door.getName(),cursor)
    print(doorSen.getName())
    print(doorSen.getDeviceName())
    print(doorSen.getOCSID())
    print(doorSen.getState())
    doorSen.updateOpen()
    print(doorSen.getState())
    doorSen.updateClosed()
    print(doorSen.getState())
    print("------------------------------------------------------")

    tempS1=tempSensor("OvenTS",oven.getName(),cursor)
    print(tempS1.getName())
    print(tempS1.getDeviceName())
    print(tempS1.getTSID())
    print(tempS1.getTemp())
    tempS1.setTemp(100)
    print(tempS1.getTemp())


    cursor.execute("SELECT * FROM Devices")

    results = cursor.fetchall()

    print(results)

    cursor.execute("SELECT * FROM Actuators")

    results = cursor.fetchall()

    print(results)

    # cursor.execute("SELECT * FROM BrightnessSensor")

    # print(cursor.fetchall())

    db.commit()
    db.close()
main()