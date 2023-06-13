from api_calls import *
import json
start=2017
END=2022
temperature=[]
snowfall=[]
rainfall=[]
windspeed=[]

while (start<END):
    beginning=str(start)+"-01-01"
    ending=str(start)+"-01-08"
    data=getInfo("Toronto",beginning,ending)
    temps,snow,rain,wind,days=ExtractInfo(data)
    t,s,r,w=ProcessData(temps,snow,rain,wind,days)
    temperature.append(t)
    snowfall.append(s)
    rainfall.append(r)
    windspeed.append(w)
    start+=1
temps,snow,rain,wind=ProcessData(temperature,snowfall,rainfall,windspeed,days)
print(f"Total avgs: {temps}, {snow}, {rain}, {wind}")

