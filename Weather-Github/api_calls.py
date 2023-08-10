import requests
import json
from weather import Weather


END=2022 

class apiCalls:
   def _getInfo(self,location,start,end):
      '''
      Make API call and return json
      '''
      baseURL='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}/{}/?unitGroup=metric&include=days&elements=name%2Ctemp%2Cprecip%2Csnow%2Cwindspeedmean&contentType=json'
      URL=baseURL.format(location,start,end)
      r= requests.get(URL)
      data=r.json()
      return data

   def _ExtractInfo(self,data):
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

   def _ProcessData(self,temps:list,snow:list,rain:list,wind:list,num)->tuple:
         
      avg_snow=0
      avg_temp=0
      avg_rain=0
      avg_wind=0
      for i in range(0,num,1):
         avg_snow=avg_snow+snow[i]
         avg_rain+=rain[i]
         avg_wind+=wind[i]
         avg_temp+=temps[i]
      avg_snow/=num
      avg_rain/=num
      avg_wind/=num
      avg_temp/=num
      int(avg_temp)
      float(avg_snow)
      avg_snow=round(avg_snow,2)
      float(avg_rain)
      avg_rain=round(avg_rain,2)
      int(avg_wind)
      return int(avg_temp), avg_snow, avg_rain, int(avg_wind)
      
   def calculateData(self,location,start,end):
      sYear=2017
      temperature=[]
      snowfall=[]
      rainfall=[]
      windspeed=[]

      while (sYear<END):
         startDate=str(sYear)+start
         endDate=str(sYear)+end
         data=self._getInfo(location,startDate,endDate)
         temps,snow,rain,wind,days=self._ExtractInfo(data)

         t,s,r,w=self._ProcessData(temps,snow,rain,wind,days)
         temperature.append(t)
         snowfall.append(s)
         rainfall.append(r)
         windspeed.append(w)
         sYear+=1
      temps,snow,rain,wind=self._ProcessData(temperature,snowfall,rainfall,windspeed,5)

      weatherObj=Weather(location,temps,snow,rain,wind)
      
      return weatherObj
   
   
 
