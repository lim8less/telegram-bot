import requests
from datetime import datetime
import os
import pytz
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
PARAMETERS = {
            "lat": float(os.getenv("LAT")),
            "lon": float(os.getenv("LON")),
            "appid": API_KEY,
            "exclude": "current,minutely,daily",
            "units": "metric",
            "lang": "hi"
        }
emoji = None


class Bot:

    def __init__(self):
        self.weather_data = None
        self.weather_data_fn()

    def hourly_weather(self):
        global emoji
        time_now = datetime.now(pytz.timezone("Asia/Kolkata"))
        for i in range(0, 25):
            datetime_obj = datetime.fromtimestamp(int(self.weather_data[i]['dt']))
            description = self.weather_data[i]['weather'][0]["description"].title()
            forcast_id = int(self.weather_data[i]['weather'][0]["id"])
            if forcast_id < 300:
                emoji = "⛈️"
            elif forcast_id < 400:
                emoji = "🌦️"
            elif forcast_id < 500:
                emoji = "🌧️"
            elif forcast_id == 800:
                emoji = "☀️"
            elif forcast_id < 900:
                emoji = "🌤️"
            if time_now.hour == datetime_obj.hour+5:
                return f"वर्तमान समय:- {time_now.hour}:{time_now.minute}:" \
                       f"{time_now.second}\nतापमान:- {self.weather_data[i]['temp']}°C\nदबाव:- " \
                       f"{self.weather_data[i]['pressure']} hPa\nनमी:- {self.weather_data[i]['humidity']}" \
                       f"% 💧\nहवा की गति:- {self.weather_data[i]['wind_speed']}m/s 🍃\nबादल:- " \
                       f"{self.weather_data[i]['clouds']}% ☁️\nविवरण:- {description}{emoji}"
        self.weather_data_fn()
        self.hourly_weather()

    def weather_data_fn(self):
        response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
        response.raise_for_status()
        self.weather_data = response.json()["hourly"][:24]