import requests
from datetime import datetime

import time

MY_LAT = 49.252750 # Your latitude
MY_LONG = 8.879400 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
now_hour = time_now.hour
print(now_hour)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


print(iss_latitude)
print(iss_longitude)

def iss_position(func_param):
    my_lat = func_param[0]
    my_long = func_param[1]
    iss_lat = func_param[2]
    iss_long = func_param[3]
    now_hour = func_param[4]
    sunrise = func_param[5]
    sunset = func_param[6]
    if now_hour < sunrise or now_hour > sunset:
        if my_lat-5 <= iss_lat <= my_lat+5 and my_long-5 <= iss_long <= my_long+5:
            return True
    return False



    




func_param = [MY_LAT, MY_LONG, iss_latitude, iss_latitude, now_hour, sunrise, sunset]

print(iss_position(func_param))


trig = 0

# while trig < 5:
#     print(trig)
#     time.sleep(5)
#     trig += 1


