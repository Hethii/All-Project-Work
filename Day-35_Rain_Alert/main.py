import requests
import os
from twilio.rest import Client

api_key = ""
account_sid = ""
auth_token = ""

number = +12055741799
# https://api.openweathermap.org/data/2.5/forecast?lat=7.544510&lon=4.556030&appid=3b9c7a5934d411f5d62f8f8c8c4b4cb8
parameters = {
    "lat": 7.544510,
    "lon": 4.556030,
    "appid": api_key

}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
# print(response.raise_for_status())

weather_data = response.json()
# print(weather_data)
weather_condition = []
# made use of a 3-hour weather forcast. 3 x 4 == 12 hours.
# using slices:
# weather_slice = weather_data["list"][:4]
#
will_rain = False
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True.
for x in range(4):
    weather_id = weather_data["list"][x]["weather"][0]["id"]
    # print(weather)
    if weather_id < 700:
        will_rain = True
    weather_condition.append(weather_id)

# ☔
#
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an Umbrella",
        from_='twilio number',
        to='my number'
    )
    print(message.status)
# print(condition)
