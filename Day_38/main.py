import requests
import json
from datetime import datetime
import os

# change the constants below with your unique data
# you can find this on your Nutritionix page
API_KEY = os.environ.get("NUTRITIONIX_API")
NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")    
# you can find this on your sheety page
URL_SHEETY = "https://api.sheety.co/52560107c1326c82737fc21ed23de8f7/kopiaMyWorkouts/workouts"
AUTH_SHEETY = f"Bearer {os.environ.get('AUTH_SHEETY')}"
SHEETY_SHEET = "workout"
        
general_url = "https://trackapi.nutritionix.com"
    
HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": API_KEY,
}

def post_exercise():
    url = general_url + "/v2/natural/exercise"
    query = input("Tell me which exercise you did:")
    params = {
        "query": query,
        "gender":"male",
        "weight_kg": 88,
        "height_cm": 182.64,
        "age": 27
    }
    response = requests.post(url, headers=HEADERS, data=params)
    return response.json()['exercises']
    

# post_exercise()


def post_exercise_to_google_sheet(data):
    url = URL_SHEETY
    header = {
        "Content-Type": "application/json",
        "Authorization": AUTH_SHEETY
    }
    params = {
        SHEETY_SHEET: {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": data['user_input'],
            "duration": data['duration_min'],
            "calories": data['nf_calories']

        }
    }

    response = requests.post(url, headers=header, json=params)
    print(response.text)


for exercises in post_exercise():
    post_exercise_to_google_sheet(exercises)

