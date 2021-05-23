import os
from datetime import date, datetime
import requests
from dotenv import load_dotenv

load_dotenv()


def add_exercise(sport_name, duration, calories):
    headers = {
        "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
    }

    params = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": sport_name,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(os.getenv("SHEETY_ENDPOINT"),
                             json=params, headers=headers)
    print(response.json())


def get_exercise_info(exercise):
    params = {
        "query": exercise
    }

    headers = {
        "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
        "x-app-key": os.getenv("NUTRITIONIX_APP_KEY"),
        "Content-Type": "application/json"
    }

    response = requests.post(
        os.getenv("NUTRIONIX_ENDPOINT"), json=params, headers=headers)
    # response.raise_for_status()

    if response.status_code == 200:
        exercise_data = response.json()["exercises"][0]
        sport_name = exercise_data["name"]
        duration = exercise_data["duration_min"]
        calories = exercise_data["nf_calories"]
        add_exercise(sport_name, duration, calories)
    else:
        print(response.json()["message"])


exercise = input("what exercise you did?")
get_exercise_info(exercise)
