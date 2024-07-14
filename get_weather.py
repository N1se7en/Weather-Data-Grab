import requests
from datetime import datetime

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


api_key = '6d62ea7c2094b4e20bee4031f61aa5d6'
city = 'Dhaka'

weather_data = get_weather(api_key, city)
print(weather_data)