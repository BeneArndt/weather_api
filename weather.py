import urllib.request
from datetime import datetime

import ipinfo
import json
import tkinter as tk

access_token = '78ff7d567f5283'
api_key = 'c9269572210ea7a9452e0af984611e6e'
lat = 0
lon = 0


def update():
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    global lon
    lon = details.loc[8:15]
    global lat
    lat = details.loc[:7]


def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_call = url + 'lat=' + lat + '&lon=' + lon + '&appid=' + api_key
    json_data = urllib.request.urlopen(api_call).read()
    data = json.loads(json_data)
    return data


def print_weather_console(data):
    main = data['main']
    weather = data['weather'][0]['main']
    temp = round(main['temp'] - 273.15)
    time = datetime.fromtimestamp(data['dt']).strftime("%d/%m/%y")
    wind = data['wind']['speed']
    print(f'Weather: {weather}\nTemperature: {temp}\nTime: {time}\nWind: {wind}')
    print(data)


def create_window():
    root = tk.Tk()
    root.title('CurrentWeather')
    root.geometry('600x400+50+50')

    root.mainloop()


if __name__ == '__main__':
    update()
    data = get_weather()
    print_weather_console(data)
    create_window()

