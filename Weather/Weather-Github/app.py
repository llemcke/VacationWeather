from flask import Flask, render_template, request
from api_calls import apiCalls
from db_script import dbAccess
from weather import Weather
from datetime import datetime, timedelta

#Initialize constants
DB= dbAccess()
WEATHER_API= apiCalls()


app = Flask(__name__)


@app.route('/')


@app.route('/home')
def home():
   return render_template('index.html')

@app.route("/calculate",methods=['GET','POST'])
def calculate():
   if request.method=='POST':
      #Set up variables
      tempWeather=Weather(None,None,None,None,None)
      
      location_arr=[]
      tempArr=[]
      snowArr=[]
      rainArr=[]
      windArr=[]
      weather=[]
      

      locations,r_date,r_temp,r_precipitation=getInfo() #get form inputs from the user
      locations_arr=locations.split("\r\n") #convert locations selected into array
      date = datetime.strptime(r_date, '%Y/%m/%d').date()  # convert string to date object
      week = date.isocalendar().week  # get week number
      
      #start_date = date.replace(year=2017)
      start_date=date.strftime('-%m-%d')
      end_date = date + timedelta(weeks=1)
      
      end_date=end_date.strftime('-%m-%d')
      
   
      for i in range(len(locations_arr)):
         tempWeather=findData(locations_arr[i],start_date,end_date,week)
         weather.append(tempWeather)
      rank(weather,r_temp,r_precipitation)
      rankArray=sorted(weather, key=lambda t: t.ranking)
      for i in snowArr:
         print(snowArr[i])
      location_arr,tempArr,snowArr,rainArr,windArr=packData(rankArray)
   return render_template('results.html' ,location=location_arr,length=len(locations_arr),temp=tempArr,snow=snowArr, wind=windArr,rain=rainArr )

def findData(location:str,start:str,end:str,week:int):
   weatherObj= Weather(None,None,None,None,None,None)
   loc=DB.checkLocation(location)
   if (loc!=-1):
      weatherObj=DB.searchData(location,week)
      if (weatherObj.temperature == 999):
        weatherObj=WEATHER_API.calculateData(location,start,end)
        DB.addData(weatherObj,week)
   else:
      DB.addLocation(location)
      DB.addLocationTable(location)
      weatherObj=WEATHER_API.calculateData(location,start,end)
      DB.addData(weatherObj, week)
   return weatherObj

def packData(weatherArr):
   weather=Weather(None,None,None,None,None)
   location=[]
   temp=[]
   snow=[]
   rain=[]
   wind=[]
   
   for i in range(len(weatherArr)):
      weather=weatherArr[i]
      location.append(weather.location)
      temp.append(weather.temperature)
      snow.append(weather.snow)
      rain.append(weather.rain)
      wind.append(weather.wind)


   return  location, temp, snow, rain, wind
      

def rank(weatherArr, r_temp,Precip:bool):
   for i in range(len(weatherArr)):
      rank=0
      temp=abs(weatherArr[i].temperature-r_temp)
      if (temp==0):
            rank+=1
      elif(temp<=2):
            rank+=2
      elif(temp<=4):
            rank+=3
      elif(temp<=6):
            rank+=4
      elif(temp<=9):
            rank+=5
      elif(temp<=15):
            rank+=6
      else:
            rank+=10
      if Precip:
            precipitation=weatherArr[i].rain+weatherArr[i].snow
            if (precipitation==0):
               rank+=1
            elif(precipitation<=1):
               rank+=3
            elif(precipitation<=2):
               rank+=6
            elif(precipitation<=4):
               rank+=7
            else:
               rank+=10
      weatherArr[i].ranking=rank
   return


def getInfo():
   if request.method=='POST':
      locations=request.form.get('selectedLocations')
      date=request.form.get('Calendar')
      temp=request.form.get('temp')
      temp=int(temp)
      precipitation = "precipitation" in request.form
      return locations,date,temp,precipitation
   return 

if __name__ == '__main__':

   app.run(debug=True)






