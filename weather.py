import urllib.request
from datetime import datetime

import ipinfo
import json
import tkinter as tk
from tkinter import ttk

access_token = '78ff7d567f5283'
api_key = 'c9269572210ea7a9452e0af984611e6e'


def get_data():
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    lon = details.loc[8:15]
    lat = details.loc[:7]
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_call = url + 'lat=' + lat + '&lon=' + lon + '&appid=' + api_key
    json_data = urllib.request.urlopen(api_call).read()
    data = json.loads(json_data)
    return data


def get_weather(data):
    main = data['main']
    weather = data['weather'][0]['main']
    temp = round(main['temp'] - 273.15)
    time = datetime.fromtimestamp(data['dt']).strftime("%d/%m/%y, %H:%M:%S")
    wind = data['wind']['speed']
    weather_info = [weather, temp, time, wind]
    return weather_info


def print_weather_console(weather_info):
    print(
        f'Weather: {weather_info[0]}\nTemperature: {weather_info[1]}\nTime: {weather_info[2]}\nWind: {weather_info[3]}')


def pressbutton():
    print_weather_console(weather_info)


def create_window(weather):
    root = tk.Tk()
    root.title('CurrentWeather')
    root.geometry('600x400+100+100')
    tree_columns = ('Weather', 'Temperature', 'Time', 'Wind')
    button = tk.Button(
        text="Click for current Weather",
        width=50,
        height=5,
        bg="white",
        fg="black",
        command=pressbutton
    )
    tree = ttk.Treeview(root, columns=tree_columns, show='headings')
    tree.heading('Weather', text='Weather')
    tree.heading('Temperature', text='Temperature')
    tree.heading('Time', text='Time')
    tree.heading('Wind', text='Wind')

    tree.insert('', tk.END, values=(weather[0], weather[1], weather[2], weather[3]))

    tree.pack()
    button.pack()
    root.mainloop()


if __name__ == '__main__':
    data = get_data()
    weather_info = get_weather(data)
    create_window(weather_info)
