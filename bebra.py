from datetime import time
import requests


appid = 'aec6ce37f4e56a2d21e7629553a2c5a8'


def get_weather(city='Moscow'):
    appid_ = 'aec6ce37f4e56a2d21e7629553a2c5a8'
    r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},ru&limit=5&appid={appid_}')
    json_object = r.json()
    lat = json_object[0]['lat']
    lon = json_object[0]['lon']
    weather_r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid_}')
    return round(weather_r.json()['main']['temp'] - 273.15)


class Friend:
    global appid

    def __init__(self, name, city):
        self.city = city
        self.name = name
        r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},ru&limit=5&appid={appid}')
        json_object = r.json()
        self.lat = json_object[0]['lat']
        self.lon = json_object[0]['lon']

    def get_weather(self):
        weather_r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={appid}')
        return f"Current weather in {self.city} is {round(weather_r.json()['main']['temp'] - 273.15)}"

    def get_time(self):
        r = requests.get(f'https://www.timeapi.io/api/Time/current/coordinate?latitude={self.lat}&longitude={self.lon}').json()
        current_date = str(r['year']) + '/' + str(r['month']) + '/' + str(r['day'])
        current_time = str(r['hour']) + ':' + str(r['minute']) + ':' + str(r['seconds'])
        return f'Current date in {self.city} is {current_date}, current time is {current_time}'

    def __repr__(self):
        return f'Name = {self.name}, lives in {self.city}'

Bebrik = Friend('Bebra', 'Novosibirsk')
print(Bebrik.get_time())
print(Bebrik.get_weather())
# print(requests.get('https://www.timeapi.io/api/Time/current/coordinate?latitude=55&longitude=37').json())
