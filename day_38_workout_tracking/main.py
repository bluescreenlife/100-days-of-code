'''A workout logger which integrates with Google Sheets and Nutritionix API'''
import requests
from datetime import datetime
import os

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
GENDER = "MALE"
WEIGHT_KG = 75.0
HEIGHT = 172.72
AGE = 32

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/414d405e70de57c54d4c1178cc937f5a/workoutTracking/workouts"

exercise_input = input("What exercise did you do today? ")

header = {
    "x-app-id" : NUTRITIONIX_APP_ID,
    "x-app-key" : NUTRITIONIX_API_KEY
}

parameters = {
    "query" : exercise_input,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT,
    "age" : AGE
}
# input exercise
response = requests.post(url=nutritionix_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()

# add a row(s) to sheet
sheety_auth_header = {
    "authorization" : SHEETY_AUTH
}

for exercise in result["exercises"]:
    workout_data = {
        "workout" : {
            "date" : datetime.now().strftime("%m/%d/%Y"),
            "time" : datetime.now().strftime("%H:%M"),
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=workout_data, headers=sheety_auth_header)
    sheet_response.raise_for_status()
    print(sheet_response.text)