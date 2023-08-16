import requests
from pprint import pprint

API_KEY = 'ab16f45d015e34e6e8eafc3e0066874f'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)