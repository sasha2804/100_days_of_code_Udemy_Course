import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "88"
HEIGHT_CM = "180"
AGE = "36"
SHEETY_TOKEN = "myWorkout2023token"

USER_NAME = "Oleksandr1987"
PASSWORD = "Korotushko2073177041"
AUTH_HEADER = "Authorization: Basic T2xla3NhbmRyMTk4NzpLb3JvdHVzaGtvMjA3MzE3NzA0MQ=="

APP_ID = "8415494f"
API_KEY = "bd5fca52e0075cd961ec485b7ab97e00"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/cc0695d4776ce3d229e48fdb4c878708/korotushkoMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#     print(sheet_response.text)


###############Basic Authentication###############
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(
      USER_NAME, 
      PASSWORD,
  )
)


