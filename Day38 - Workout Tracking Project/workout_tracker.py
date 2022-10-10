import requests
import datetime as dt
import os

# Przy konfiguracji danego projektu w PyCharm mozna ustawic w programie Environmental variables
# Lekcja 335 (Day 38 Step 6) w pytaniach do kursu jest to pokazane
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
    }

exercises = {
     "query": input("Exercises: "),
     "gender": "male",
     "weight_kg": 91.8,
     "height_cm": 193,
     "age": 28
    }


exercise_response = requests.post(url=exercise_endpoint, json=exercises, headers=headers)
exercises = exercise_response.json()
print(exercises)

sheety_endpoint_post = os.environ.get("SHEET_ENDPOINT")

current_time = dt.datetime.strftime(dt.datetime.now(), "%H:%M")
current_date = dt.datetime.strftime(dt.datetime.now(), "%d/%m/%Y")


for exercise in exercises["exercises"]:
    sheet_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Zamiast tego moze tez byc username i haslo stworzone na stronie API
    # Wtedy zamiast slownika jest auth=(USERNAME, PASSWORD)
    headers = {
        "Authorization": os.environ.get("TOKEN")
    }

    sheety_response = requests.post(url=sheety_endpoint_post, json=sheet_data, headers=headers)
    print(sheety_response.text)
