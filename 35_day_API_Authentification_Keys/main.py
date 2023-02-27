
import requests

url_weather = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

twilio_code = "0yFJM4r-cziFI9FS9sFftUY-7lH0H1JrRUnj6ePf" 
'''
If you lose your phone, or don't have access to your verification device, this code is your failsafe to access your account.
'''
twilio_trial_number = "+12766249742"


# import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC1e639d993da7c887ff46e248d39e8d61'
auth_token = '49728e3b08f434fc84d46f5ded905473'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12766249742',
                     to='+380978308027'
                 )

print(message.sid)





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



    
    
