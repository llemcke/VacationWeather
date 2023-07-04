
# Importing module
import mysql.connector
mydb = mysql.connector.connect(
        host = "aws.connect.psdb.cloud",
        user = "4ih7tdzdlejo6b6dlf00",
        password = "pscale_pw_Fg0UH4nU15vcCqbemPhmofGN63ZRg2soU3YQNppPVR2",
        database= "weatherdata"
    )
cursor=mydb.cursor(buffered=True)

#connect to database
    
def checkLocation(location):
    str=f'SELECT id FROM Locations WHERE location ="{location}"'
    cursor.execute(str)
    chk=cursor.fetchone()
    if chk==None:
         chk=-1
    return chk

def addLocation(location):
    str=f'INSERT INTO Locations (id, location) VALUES (default,"{location}")'
    cursor.execute(str)
    return

def addLocationTable(location):
    str=f'CREATE TABLE {location}(week INT, temp FLOAT, snow INT, rain FLOAT, wind INT, PRIMARY KEY(week));'
    cursor.execute(str)
    return 

def addData(location, week, temp, snow, rain, wind):
    str=f'INSERT INTO {location} (week, temp, snow, rain, wind) VALUES({week},{temp},{snow},{rain},{wind})'
    cursor.execute(str)
    return

def searchData(location, week):
    cursor = mydb.cursor(dictionary=True)
    str=f'SELECT temp, snow, rain, wind FROM {location} WHERE week="{week}"'
    cursor.execute(str)
    result=cursor.fetchall()
    for row in result:
        t=row["temp"]
        s=row["snow"]
        r=row["rain"]
        w=row["wind"]
    return t,s,r,w

