
import requests

url_weather = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"


lat = 49.252750
lon = 8.879400
api_key = "3bef3c17fb5292d10c2768155ff15bcd"

parameters = {
    "lat" : lat,
    "lon" : lon, 
    "appid" : api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url= f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={parameters["exclude"]}&appid={api_key}', params=parameters)
response.raise_for_status()
current_weather = response.json()



# print(current_weather)
# print('\n')
# # cut = current_weather['hourly'][0]['weather'][0]['id']
# cut = current_weather['hourly'][0]['weather']
# print(type(cut))
# print(cut)

id_set = set()

for hour in range(0,13):
    weather_id = current_weather['hourly'][hour]['weather'][0]['id']
    id_set.add(int(weather_id))      
    
def umbrella_check(id_set):
    for i in id_set:
        if i < 700:
            return 'Get your umbrella'
    return 'You do not need umbrella today'

print(umbrella_check(id_set))



    
    
