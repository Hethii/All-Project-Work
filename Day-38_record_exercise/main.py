import requests
from datetime import datetime
import os

USERNAME = os.environ['SHEETY_USERNAME']
PASSWORD = os.environ['SHEETY_PASSWORD']
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']

today = datetime.now()
present_time = today.strftime("%X")
formatted_time = today.strftime("%d/%m/%Y")

user_headers = {
    "x-app-id": os.environ["NIX_APP_ID"],
    "x-app-key": os.environ["NIX_API_KEY"],
    "x-remote-user-id": "0"
}
user_params = {
    "query": input("Tell me which exercise you did: "),
    # "query": "ran 5k and cycled 28 minutes",
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 173.00,
    "age": 25
}

response1 = requests.post(url=exercise_endpoint, json=user_params, headers=user_headers)
data_result = response1.json()

for exercise in data_result["exercises"]:
    sheety_params = {
        'workout':
        {
            'date': formatted_time,
            'time': present_time,
            'exercise': exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"],
        }
    }
    response2 = requests.post(url=SHEETY_ENDPOINT,
                              json=sheety_params,
                              auth=(USERNAME, PASSWORD))
    print(response2.raise_for_status())
    print(response2.text)
# sheety_endpoint = f"{SHEETY_ENDPOINT}"
# response = requests.get(url=sheety_endpoint, auth=(USERNAME, PASSWORD))
# print(response.text)
