import requests
import pandas as pd
from datetime import datetime
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')
print(api_key)

cities = ["New York", "Boston", "San Francisco", "Los Angeles", "Seattle", "Chicago", "Miami", "Las Vegas", "Denver", "Minneapolis"]
data = []


# STEP 1: Ingest the data
# iterate through each city on the list
for city in cities:
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    )

    # create dictionaries for each city 
    res = weather_data.json()
    if weather_data.json()["cod"]  == 200: 
        city_data = {
            "city": city,
            "weather": res["weather"][0]["main"],
            "description": res["weather"][0]["description"],
            "temperature": res["main"]["temp"],
            "temp_min": res["main"]["temp_min"],
            "temp_max": res["main"]["temp_max"],
            "humidity": res["main"]["humidity"],
            "wind_speed": res["wind"]["speed"]
        }
         
        # add the data to the list
        data.append(city_data)


# STEP 2: Transform data
# use pandas to create the data frame
data_frame = pd.DataFrame(data)

# added time stamp and celsius
data_frame["celsius"] = ((data_frame["temperature"] - 32) * 5/9).round(2)
data_frame["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")
print(data_frame)


#STEP 3: Loading the data with sql (using sql lite 3)
#this connects/creates the weather database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

data_frame.to_sql("weather", conn, if_exists='replace', index=False)

#testing some queries
print("Some US Cities: ")
for row in cursor.execute("""Select city, 
                            temperature || "°F" AS temp_imperial,
                            celsius || "°C" AS temp_metric,
                            humidity || "%" AS humidity FROM weather"""):
    print(row)

print("\n")
print("Hottest City: ")
for row in cursor.execute("""SELECT city, 
                            MAX(temperature) || "°F" AS max_imperial,
                          MAX(celsius) || "°C" AS max_metric FROM weather"""):
    print(row)

print("\n")
print("Top 5 windiest cities: ")
for row in cursor.execute("""SELECT city, 
                          wind_speed || " mph" AS wind_speed FROM weather ORDER BY wind_speed DESC LIMIT 5"""):
    print(row)
