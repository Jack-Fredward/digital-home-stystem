import pymysql
from device import *
from commomsim import *
from kitchensim import *
from kitchen import *
from login import *
from diningRoom import *
from study import *
from breakfastNook import *
from laundryRoom import *
from laundryRoomSim import *
from masterBedroom import *
from mainDoor import *
from mainDoorSim import *
from bedroom import *
from halfBath import *
from bathroom import *
from masterBathroom import *
from livingRoom import *
from healthSystemSim import *




def main():
    # Open database connection
    db = pymysql.connect("localhost","jp","Database","digital_home_database" )

    # prepare a cursor object using cursor() method
    dbCursor = db.cursor()
    
    dbCursor.execute("DELETE FROM TempSensors")
    dbCursor.execute("DELETE FROM OpenCloseSensors")
    dbCursor.execute("DELETE FROM MotionSensors")
    dbCursor.execute("DELETE FROM LiquidFlowSensors")
    dbCursor.execute("DELETE FROM BrightnessSensor")
    dbCursor.execute("DELETE FROM Actuators")
    dbCursor.execute("DELETE FROM Devices")

    kitchen1=kitchen("kitchen", dbCursor)
    diningRoom1=diningRoom("dining room",dbCursor)
    study1 = study("study",dbCursor)
    breakfastNook1 = breakfastNook("breakfast nook",dbCursor)
    laundryRoom1 = laundryRoom("laundry room", dbCursor)
    masterBedroom1 = masterBedroom("master bedroom", dbCursor)
    mainDoor1 = mainDoor("Main Door",dbCursor)
    bedRoom2 = bedRoom("bedroom2","2",dbCursor,0)
    bedRoom3 = bedRoom("bedroom3", "3", dbCursor, 0)
    bedRoom4 = bedRoom("bedroom4", "4", dbCursor, 1)
    halfBathroom1 = halfBathroom("halfbathroom", dbCursor)
    bathroom2 = bathroom("bathroom2", "2", dbCursor, 0, 0, 0)
    bathroom3 = bathroom("bathroom3", "3", dbCursor, 0, 1, 0)
    bathroom4 = bathroom("bathroom4", "4", dbCursor, 1, 0, 1)
    masterBathroom1 = masterBathroom("masterbathroom", dbCursor)
    livingRoom1 = livingRoom("livingRoom", dbCursor)


    allExternalDoors = [mainDoor1, laundryRoom1.door[1], bedRoom4.doors[1], bathroom4.doors[1],masterBedroom1.doors[1],livingRoom1.doors[0]]
    allWindows = [diningRoom1.windows[0], study1.windows[0], breakfastNook1.windows[0], breakfastNook1.windows[1], masterBedroom1.windows[0], masterBedroom1.windows[1], masterBedroom1.windows[2], masterBedroom1.windows[3], bedRoom2.windows[0], bedRoom2.windows[1], bedRoom3.windows[0], bedRoom3.windows[1], bedRoom4.windows[0], bedRoom4.windows[1], bathroom2.windows[0], bathroom3.windows[0], bathroom4.windows[0], masterBathroom1.windows[0], masterBathroom1.windows[1], masterBathroom1.windows[2], masterBathroom1.windows[3], masterBathroom1.windows[4]]

    # mainDoor1.getName())

    for door in allExternalDoors:
        print(door.getName())

    for window in allWindows:
        print(window.getName())



    study1.windows[0].sensors[0].updateOpen()
    db.commit()

    dbCursor.execute("SELECT Devices.D_Name, OpenCloseSensors.State FROM Devices INNER JOIN OpenCloseSensors ON Devices.D_ID=OpenCloseSensors.D_ID WHERE (D_Name  LIKE '%Window%' OR D_Name LIKE '%Door%');")

    results = dbCursor.fetchall()

    study1.windows[0].sensors[0].updateOpen()
    db.commit()


    for i in range(len(results)):
        # print(results[i][0]+ " "+str(results[i][1]))
        if results[i][1]==1:
            print("Intruder alert!!!")
            print(results[i][0]+ " "+str(results[i][1]))
            
    db.commit()
    db.close()




main()