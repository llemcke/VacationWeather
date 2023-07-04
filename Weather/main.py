from api_calls import calculateData
import json
from db_script import *
import mysql.connector

end="-01-08"
start="-01-01"
location="Ottawa_Ontario"
week=1
Loc=checkLocation(location)
if (Loc!=-1):
    temp,snow,rain,wind=searchData(location,week)
    if temp is None:
        temp,snow,rain,wind=calculateData(location,start,end)
        addData(location, week, temp, snow, rain, wind)
else:
    addLocation(location)
    addLocationTable(location)
    temp,snow,rain,wind=calculateData(location,start,end)
    addData(location, week, temp, snow, rain, wind)

print(temp)
print(snow)
print(rain)
print(wind)
cursor.close()








