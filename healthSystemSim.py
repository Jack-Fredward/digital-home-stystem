import pymysql
from masterBedroom import *
import datetime
import time
import random as rand
import math

def simBloodPressure(frame, masterBedroom, db,controller):
    masterBedroom.setBloodPressureMonitorTopNumber(rand.randint(40, 180))
    masterBedroom.setBloodPressureMonitorBottomNumber(rand.randint(40, 120))

    # print("BP: "+str(masterBedroom.getBloodPressureMonitorTopNumber())+"/"+str(masterBedroom.getBloodPressureMonitorBottomNumber()))

    frame.bloodPressureTopNumberLabel.config(text=str(masterBedroom.getBloodPressureMonitorTopNumber()))
    frame.bloodPressureBottomNumberLabel.config(text=str(masterBedroom.getBloodPressureMonitorBottomNumber()))
    frame.update()

    if (40<=masterBedroom.getBloodPressureMonitorTopNumber() and masterBedroom.getBloodPressureMonitorTopNumber()<90) and (40<=masterBedroom.getBloodPressureMonitorBottomNumber() and masterBedroom.getBloodPressureMonitorBottomNumber()<60):
        controller.popupmsg("Low Blood Pressure")
    elif (90<=masterBedroom.getBloodPressureMonitorTopNumber() and masterBedroom.getBloodPressureMonitorTopNumber()<120) and (60<=masterBedroom.getBloodPressureMonitorBottomNumber() and masterBedroom.getBloodPressureMonitorBottomNumber()<80):
        controller.popupmsg("Normal Blood Pressure")
    elif (120<=masterBedroom.getBloodPressureMonitorTopNumber() and masterBedroom.getBloodPressureMonitorTopNumber()<130) and (masterBedroom.getBloodPressureMonitorBottomNumber()<80):
        controller.popupmsg("Elevated Blood Pressure(prehypertension)")
    elif (130<=masterBedroom.getBloodPressureMonitorTopNumber() and masterBedroom.getBloodPressureMonitorTopNumber()<140) and (80<=masterBedroom.getBloodPressureMonitorBottomNumber() and masterBedroom.getBloodPressureMonitorBottomNumber()<90):
        controller.popupmsg("High Blood Pressure (Hypertension) Stage 1")
    elif (140<=masterBedroom.getBloodPressureMonitorTopNumber() and masterBedroom.getBloodPressureMonitorTopNumber()<180) and (90<=masterBedroom.getBloodPressureMonitorBottomNumber() and masterBedroom.getBloodPressureMonitorBottomNumber()<120):
        controller.popupmsg("High Blood Pressure (Hypertension) Stage 2")
    elif (180<=masterBedroom.getBloodPressureMonitorTopNumber()) or (120<=masterBedroom.getBloodPressureMonitorBottomNumber()):
        controller.popupmsg("Hypertensive crisis (consult doctor immediately)")
    else:
        simBloodPressure(frame,masterBedroom, db,controller)

def simHeartRate(frame, masterBedroom, db, controller, age, gender):
    age = int(age)
    
    if gender == 1: #male
        if (18<=age<=25):
            lowerBoundHR = [49, 56, 62, 66, 70, 74, 82]
            upperBoundHR = [55, 61, 65, 69, 73, 81, 82]
        elif(26<=age<=35):
            lowerBoundHR = [49, 55, 62, 66, 71, 75, 82]
            upperBoundHR = [54, 61, 67, 70, 74, 81, 82]
        elif(36<=age<=45):
            lowerBoundHR = [50, 57, 63, 67, 71, 76, 83]
            upperBoundHR = [56, 62, 66, 70, 75, 82, 83]
        elif(46<=age<=55):
            lowerBoundHR = [50, 58, 64, 68, 72, 77, 84]
            upperBoundHR = [57, 63, 67, 71, 76, 83, 84]
        elif(56<=age<=65):
            lowerBoundHR = [51, 57, 62, 68, 72, 76, 82]
            upperBoundHR = [56, 61, 67, 71, 75, 81, 82]
        else:
            lowerBoundHR = [50, 56, 62, 66, 70, 74, 80]
            upperBoundHR = [55, 61, 65, 69, 73, 79, 80]
    elif gender == 2: #female
        if (18<=age<=25):
            lowerBoundHR = [54, 61, 66, 70, 74, 79, 85]
            upperBoundHR = [60, 65, 69, 73, 78, 84, 85]
        elif(26<=age<=35):
            lowerBoundHR = [54, 60, 65, 69, 73, 77, 83]
            upperBoundHR = [59, 64, 68, 72, 76, 82, 83]
        elif(36<=age<=45):
            lowerBoundHR = [54, 60, 65, 70 ,74, 79, 85]
            upperBoundHR = [59, 64, 69, 73, 78, 84, 85]
        elif(46<=age<=55):
            lowerBoundHR = [54, 61, 66, 70, 74, 78, 84]
            upperBoundHR = [60, 65, 69, 73, 77, 78, 83]
        elif(56<=age<=65):
            lowerBoundHR = [54, 60, 65, 69, 74, 78, 84]
            upperBoundHR = [59, 64, 68, 73, 77, 83, 84]
        else:
            lowerBoundHR = [54, 60, 65, 69, 73, 77, 85]
            upperBoundHR = [59, 64, 68, 72, 76, 84, 85]


    if gender ==1:
        heartRate = rand.randint(lowerBoundHR[0], upperBoundHR[6]+math.floor((age/2)))
    elif gender == 2:
        heartRate = rand.randint(lowerBoundHR[0], upperBoundHR[6]+math.floor((age/4)))
    masterBedroom.setHeartRate(heartRate)
    frame.heartRateValueLabel.config(text=str(heartRate))
    frame.update()
    db.commit()

    heartRateClassification = { 0: "Athlete",
                                1: "Excellent",
                                2: "Great",
                                3: "Good",
                                4: "Average",
                                5: "Below Average",
                                6: "Poor"}
    
    for i in range(7):
        if lowerBoundHR[i]<=heartRate<=upperBoundHR[i]:
            controller.popupmsg("Heart Rate Condition: "+heartRateClassification[i])
        elif upperBoundHR[6]<=heartRate:
            controller.popupmsg("Warning high resting heart rate consult doctor")
    

