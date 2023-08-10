
from api_calls import apiCalls
from db_script import dbAccess
from weather import Weather
api=apiCalls()
access=dbAccess()
weatherObj=Weather(None,None,None,None,None)
end="-02-02"
start="-01-31"
location="London_Ontario"
week=1
weatherObj=api.calculateData(location,start,end)
print(weatherObj.temperature)

'''
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

import requests
import json
baseURL='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}/{}/?unitGroup=metric&include=days&elements=name%2Ctemp%2Cprecip%2Csnow%2Cwindspeedmean&key=GALF82QEG92EWFFSJTU36BKHG&contentType=json'
URL=baseURL.format("Toronto","2023-06-05","2023-06-06")
r= requests.get(URL)
data=r.json()
print(data)
'''






