# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# import smtplib

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notify_data = NotificationManager()

ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_codes(row["city"])
    # print(f"sheet_data:\n {sheet_data}")
    data_manager.sheet_details = sheet_data
    data_manager.update_destination_code()

for destination in sheet_data:
    # print(destination["lowestPrice"])
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today)
    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        text = f"""Low price alert!, only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"""
        if flight.stop_overs > 0:
            text += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(text)
        notify_data.notify_manager(text)

# notify_data.notify_manager()
