
# Importing module
import mysql.connector
from weather import Weather
mydb = mysql.connector.connect(
        host = "aws.connect.psdb.cloud",
        user = *,
        password = *,
        database= "weatherdata"
    )
class dbAccess():
        
    def checkLocation(self, location:str)->int:
        cursor=mydb.cursor(buffered=True)
        str=f'SELECT id FROM Locations WHERE location ="{location}"'
        cursor.execute(str)
        chk=cursor.fetchone()
        if chk==None:
            chk=-1
        mydb.commit()
        cursor.close()
        return chk

    def addLocation(self,location:str):
        cursor=mydb.cursor(buffered=True)
        str=f'INSERT INTO Locations (id, location) VALUES (default,"{location}")'
        cursor.execute(str)
        mydb.commit()
        cursor.close()
        return

    def addLocationTable(self,location:str):
        cursor=mydb.cursor(buffered=True)
        str=f'CREATE TABLE {location}(week INT, temp INT, snow INT, rain INT, wind INT, PRIMARY KEY(week));'
        cursor.execute(str)
        mydb.commit()
        cursor.close()
        return 

    def addData(self, weatherObj:Weather,week:int):
        cursor=mydb.cursor(buffered=True)
        str=f'INSERT INTO {weatherObj.location} (week, temp, snow, rain, wind) VALUES({week},{weatherObj.temperature},{weatherObj.snow},{weatherObj.rain},{weatherObj.wind});'
        cursor.execute(str)
        mydb.commit()
        cursor.close()
        return

    def searchData(self, location:str, week:int)->Weather:
        
        cursor = mydb.cursor(dictionary=True)
        str=f'SELECT temp, snow, rain, wind FROM {location} WHERE week="{week}"'
        cursor.execute(str)
        result=cursor.fetchone()
        if result is None:
            t=999
            s=999
            r=999
            w=999
        else:
            t=result["temp"]
            s=result["snow"]
            r=result["rain"]
            w=result["wind"]
        weatherObj= Weather(location,t,s,r,w)
        mydb.commit()
        cursor.close()
        return weatherObj

