import requests
import os
# from pprint import pprint
# This class is responsible for talking to the Google Sheet.
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

# print(SHEETY_ENDPOINT, USERNAME, PASSWORD)
class DataManager:
    def __init__(self):
        self.sheet_details = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=(USERNAME, PASSWORD))
        self.sheet_details = response.json()["prices"]

        return self.sheet_details

    def update_destination_code(self):
        for city in self.sheet_details:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=(USERNAME, PASSWORD)
            )
            print(response.text)


