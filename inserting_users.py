# inserting_users.py
# JP
# Description: This will add the main users of our digital home system
# Input      : Names and relevant information of each user
# Onput      : Database will be updated to relfect new users

import pymysql

# Open database connection
db = pymysql.connect("localhost","jp","Database","digital_home_database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# prepping info to be inserted
sql = "INSERT INTO Users (F_Name, L_Name, Age, Is_Disabled, Is_SU) VALUES (%s, %s, %s, %s, %s);"

val = [["Steve", "Wright", 76, 1, 0],['Mini', 'Wright', 72, 0, 0],['Stanely', 'Wright', 47, 0, 1], ['Vinni', 'Wright', 42, 0, 0], ['Michelle', 'Wright', 18, 0, 0], ['Robert', 'Wright', 16, 0,0]]


for i in range(6):
    print(val[i])
    cursor.execute(sql,val[i])


cursor.execute("SELECT * FROM Users")

results = cursor.fetchall()

print(results)
db.commit()
db.close()