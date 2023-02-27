
import requests
from twilio.rest import Client

url_weather = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
twilio_code = "0yFJM4r-cziFI9FS9sFftUY-7lH0H1JrRUnj6ePf" 
'''
If you lose your phone, or don't have access to your verification device, this code is your failsafe to access your account.
'''
twilio_trial_number = "+12766249742"


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC1e639d993da7c887ff46e248d39e8d61'
auth_token = '146171db2b6cef93b3f62e6456cbc818'
client = Client(account_sid, auth_token)


lat = 39.961178
lon = -82.998795
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


id_set = set()

for hour in range(0,13):
    weather_id = current_weather['hourly'][hour]['weather'][0]['id']
    id_set.add(int(weather_id))      
    
def umbrella_check(id_set):
    for i in id_set:
        if i < 700:
            return 1          
    return 0

if umbrella_check(id_set) == 1:
    message = client.messages \
                .create(
                     body="Get your umbrella!!! It's gonna rain",
                     from_='+12766249742',
                     to='+380978308027'
                 )
    print(message.sid)
    print('it works')








    
    
