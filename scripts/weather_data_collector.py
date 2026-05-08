import requests
import pandas as pd
import os

from datetime import datetime

from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/"


cities = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", 
    "Chennai", "Kolkata", "Surat", "Pune", "Jaipur", 
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", 
    "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara", 
    "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad", 
    "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", 
    "Bareilly", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", 
    "Srinagar", "Ranchi", "Howrah", "Coimbatore", "Jabalpur", 
    "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur", 
    "Kota", "Guwahati", "Chandigarh", "Solapur", "Aligarh"
]



def get_weather_data(city):

    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"{city}: {response.status_code}")
            return None

        data = response.json()

        weather_data = {

            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),

            'city': data['name'],

            'current_temp': round(data['main']['temp']),

            'feels_like': round(data['main']['feels_like']),

            'humidity': data['main']['humidity'],

            'wind_speed': data['wind']['speed'],

            'weather_description': data['weather'][0]['description'],

            'temp_min': round(data['main']['temp_min']),

            'temp_max': round(data['main']['temp_max']),

            'pressure': data['main']['pressure'],

            'country': data['sys']['country'],

            'visibility': data.get('visibility', 0)

        }

        return weather_data

    except Exception as e:

        print(f"Exception occurred: {e}")

        return None


all_weather_data = []

for city in cities:

    weather = get_weather_data(city)

    if weather:
        all_weather_data.append(weather)

df = pd.DataFrame(all_weather_data)
CSV_FILE = "/home/Aqib/Desktop/weather_forecast/weather_data.csv"

file_exists = os.path.isfile(CSV_FILE)

df.to_csv(
    CSV_FILE,
    mode='a',
    index=False,
    header=not file_exists
)

print("Weather data saved successfully")