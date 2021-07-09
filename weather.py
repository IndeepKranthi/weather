import requests
import os
from datetime import datetime
import pandas as pd
import json
import csv

user_api = "a972fae8c93f1cdacc59df4babb43e21"

location = ['texas','michigan']

length = len(location)

for i in range(length):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location[i]+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    city_name =  api_data['name']
    temp_city = ((api_data['main']['temp']) - 273.15)
    city_temp_f = (temp_city * 1.8) + 32
    city_temperature = "{:.2f}".format(city_temp_f)+" F"
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    input_variable = [city_name,city_temperature, weather_desc, hmdt,date_time]
    with open('Example.csv','a', newline = '') as appendobj: 
        append=csv.writer(appendobj)
        append.writerow(input_variable)

'''
with open('Example.csv', 'w', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ',')
    my_writer.writerow(input_variable)

with open('data.txt') as json_file:
    data = json.load(json_file)
    print ("name:", data['name'],end = ',')
           # print ("temp:", y('temp'),end = ',')
    
    for x in data['weather']:
        print("description is: ", x['description'])

    for y in data['main']:
        print ("temp: ", y['main']['temp'], end = ',')
    
    for y in data:
    #If Json Field value is a Nested Json
        if (isinstance(data['main'], dict)):checkDict(data[element], element)
    
    
       
        



   
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%Y-%M-%D %H:%M:%S ")

if "name" in api_data:print(api_data["name"], end = ',')

def formeln(c):
    F = 9.0/5.0 * temp_city + 32
    return F

def printC(Temp_f):
    Temp_f = str(Temp_f)
    print (Temp_f + " C", end = ',')
print (weather_desc, end = ',')
print (hmdt, '%', end = ',')
print (wind_spd ,'kmph', end = ',')
print(date_time)

a_file = open("weather.csv", "w")
text = "abc\n123"
print(text, file=a_file)
a_file.close()



df = ['hmdt','temp_city','weather_desc']
#df['date.pretty'] = pd.to_datetime(df['date.pretty'])
 
print(df)
 
# Create CSV
df.to_csv('weather.csv')
 
# Append CSV
#df.to_csv('C:\WeatherUnderGround\Test.csv', na_rep='-99999', columns=None, header=False, index=True, index_label=None, mode='a')
'''