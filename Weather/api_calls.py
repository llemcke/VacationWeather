
from pip._vendor import requests
import json

start=2017
END=2022 

def getInfo(location,start,end):
   '''
   Make API call and return json
   '''
   baseURL=' https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}/{}/?unitGroup=metric&include=days&elements=name%2Ctemp%2Cprecip%2Csnow%2Cwindspeedmean&key=GALF82QEG92EWFFSJTU36BKHG&contentType=json'
   URL=baseURL.format(location,start,end)
   r= requests.get(URL)
   data= r.json()
   return data

def ExtractInfo(data):
   '''
   extract info from days in json data
   '''
   days=data['days']
   temps=[]
   rain=[]
   snow=[]
   wind=[]

   for d in days:
      
      if d['precip'] is None:
         p=0.0
      else:
         p=d['precip']

      if d['snow'] is None:
         s=0.0
      else:
         s=d['snow']
         
      t=d['temp']
      w=d['windspeedmean']
      temps.append(t)
      snow.append(s)
      rain.append(p)
      wind.append(w)
      
   return temps,snow,rain,wind,len(days)

def ProcessData(temps,snow,rain,wind,days):
      
   avg_snow=0
   avg_temp=0
   avg_rain=0
   avg_wind=0
   for i in range(0,days,1):
      avg_snow=avg_snow+snow[i]
      avg_rain+=rain[i]
      avg_wind+=wind[i]
      avg_temp+=temps[i]
   avg_snow/=7
   avg_rain/=7
   avg_wind/=7
   avg_temp/=7
   return int(avg_temp), int(avg_snow), float(avg_rain), int(avg_wind)
   
def calculateData(location,start,end):
   sYear=2017
   temperature=[]
   snowfall=[]
   rainfall=[]
   windspeed=[]

   while (sYear<END):
      beginning=str(sYear)+start
      ending=str(sYear)+end

      data=getInfo(location,beginning,ending)
      temps,snow,rain,wind,days=ExtractInfo(data)

      t,s,r,w=ProcessData(temps,snow,rain,wind,days)
      temperature.append(t)
      snowfall.append(s)
      rainfall.append(r)
      windspeed.append(w)
      sYear+=1
   temps,snow,rain,wind=ProcessData(temperature,snowfall,rainfall,windspeed,5)
   return temps,snow,rain,wind
