import requests

url_weather = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

lat = 49.252750
lon = 8.879400
api_key = '3bef3c17fb5292d10c2768155ff15bcd'

parameters = {
    'lat' : lat,
    'lon' : lon, 
    'appid' : api_key,
}

response = requests.get(url= f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}', params=parameters)
response.raise_for_status()
current_weather = response.json()

print(current_weather)



