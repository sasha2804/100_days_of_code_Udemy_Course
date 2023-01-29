
# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.json()['iss_position']['longitude'])


import requests
from datetime import datetime

parameters = {
    'lat': 50.110880,
    'long': 8.679490,
    'formatted':0
}

response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()

data =  response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(data)
# print(type(sunrise))
print(sunset.split('T')[1].split(':')[0])
print(sunrise.split('T')[1].split(':')[0])

time_now = datetime.now()

print(time_now.hour)

x = 10
z = 25

y = 11

if y < x or y > z:
    print('OK')