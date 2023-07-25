from api_calls import apiCalls
from db_script import dbAccess
from weather import Weather
api=apiCalls()
access=dbAccess()
weatherObj=Weather(None,None,None,None,None)
end="-01-08"
start="-01-01"
location="London_Ontario"
week=1


Loc=access.checkLocation(location)
if (Loc!=-1):
    weatherObj=access.searchData(location,week)
    if (weatherObj.temperature == 999):
        weatherObj=api.calculateData(location,start,end)
        access.addData(weatherObj,week)
else:
    access.addLocation(location)
    access.addLocationTable(location)
    weatherObj=api.calculateData(location,start,end)
    access.addData(weatherObj, week)

print(weatherObj.temperature)
print(weatherObj.snow)
print(weatherObj.rain)
print(weatherObj.wind)








