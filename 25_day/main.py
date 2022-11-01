import pandas as pd

with open('25_day/weather_data.csv') as data:
    data = data.readlines()

print(data)