from flask import Flask, render_template, request, flash
from api_calls import apiCalls
from anyascii import anyascii
from db_script import dbAccess
from weather import Weather
from datetime import datetime, timedelta

#Initialize constants
DB = dbAccess()
WEATHER_API = apiCalls()

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"


@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html')


@app.route("/calculate", methods=['GET', 'POST'])
def calculate():
  if request.method == 'POST':
    #Set up variables
    tempWeather = Weather(None, None, None, None, None)

    location_arr = []
    tempArr = []
    snowArr = []
    rainArr = []
    windArr = []
    weather = []
    rankArr = []
    locations, r_date, r_temp, r_precipitation = getInfo(
    )  #get form inputs from the user
    try:
      r_temp = int(r_temp)
    except:
      flash("Target Temperature must be a number")
      return render_template('index.html',
                             date=r_date,
                             selectedLocations=locations)
    locations_arr = locations.split(
      "\r\n")  #convert locations selected into array

    date = datetime.strptime(
      r_date, '%Y/%m/%d').date()  # convert string to date object
    week = date.isocalendar().week  # get week number

    start_date = date.strftime('-%m-%d')
    end_date = date + timedelta(weeks=1)

    end_date = end_date.strftime('-%m-%d')

    for i in range(len(locations_arr)):
      string = locations_arr[i]
      string = string.replace(",", "_")
      string = string.replace(" ", "_")
      string = string.replace("-", "_")
      string = anyascii(string)
      try:
        tempWeather = findData(string, start_date, end_date, week)
      except:
        flash("Invalid location selected, please try again")
        return render_template('index.html', temp=r_temp, date=r_date)
      weather.append(tempWeather)
    rank(weather, r_temp, r_precipitation)
    rankArray = sorted(weather, key=lambda t: t.ranking)
    location_arr, tempArr, snowArr, rainArr, windArr, rankArr = packData(
      rankArray)
    for i in range(len(location_arr)):
      location_arr[i] = location_arr[i].replace("__", ", ")
      location_arr[i] = location_arr[i].replace("_", " ")

  return render_template('results.html',
                         location=location_arr,
                         length=len(locations_arr),
                         temp=tempArr,
                         snow=snowArr,
                         wind=windArr,
                         rain=rainArr,
                         rank=rankArr)


def findData(location: str, start: str, end: str, week: int):
  weatherObj = Weather(None, None, None, None, None, None)
  loc = DB.checkLocation(location)
  if (loc != -1):
    weatherObj = DB.searchData(location, week)
    if (weatherObj.temperature == 999):
      weatherObj = WEATHER_API.calculateData(location, start, end)
      DB.addData(weatherObj, week)
  else:
    DB.addLocation(location)
    DB.addLocationTable(location)
    weatherObj = WEATHER_API.calculateData(location, start, end)
    DB.addData(weatherObj, week)
  return weatherObj


def packData(weatherArr):
  weather = Weather(None, None, None, None, None)
  location = []
  temp = []
  snow = []
  rain = []
  wind = []
  rank = []

  for i in range(len(weatherArr)):
    weather = weatherArr[i]
    location.append(weather.location)
    temp.append(weather.temperature)
    snow.append(weather.snow)
    rain.append(weather.rain)
    wind.append(weather.wind)
    rank.append(weather.ranking)

  return location, temp, snow, rain, wind, rank


def rank(weatherArr, r_temp, Precip: bool):
  for i in range(len(weatherArr)):
    rank = 0
    temp = abs(weatherArr[i].temperature - r_temp)
    if (temp == 0):
      rank += 1
    elif (temp <= 2):
      rank += 2
    elif (temp <= 4):
      rank += 3
    elif (temp <= 6):
      rank += 4
    elif (temp <= 9):
      rank += 5
    elif (temp <= 15):
      rank += 6
    else:
      rank += 10
    if Precip:
      precipitation = weatherArr[i].rain + weatherArr[i].snow
      if (precipitation == 0):
        rank += 1
      elif (precipitation <= 1):
        rank += 3
      elif (precipitation <= 2):
        rank += 6
      elif (precipitation <= 4):
        rank += 7
      else:
        rank += 10
    weatherArr[i].ranking = rank
  return


def getInfo():
  if request.method == 'POST':
    locations = request.form.get('selectedLocations')

    date = request.form.get('Calendar')
    temp = request.form.get('temp')

    checked = 'check' in request.form
    print(checked)
    if (checked == 1):
      B_precipitation = True
    else:
      B_precipitation = False
    return locations, date, temp, B_precipitation
  return


if __name__ == '__main__':

  app.run(host='0.0.0.0', port=8080)
