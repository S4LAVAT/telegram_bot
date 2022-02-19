import requests 
import json
from dotenv import load_dotenv
import os


load_dotenv()
API_key = os.environ.get('Open_weather_API_key')

def get_weather(city):
	url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=ru"

	response = requests.get(url)
	dict_response = json.loads(response.text)
	weather = dict_response.get('weather')[0].get('description')
	degrees = dict_response.get('main').get('temp')
	return weather, degrees




