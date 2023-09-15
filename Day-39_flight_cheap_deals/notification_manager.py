import smtplib
import os
from twilio.rest import Client
from smtplib import SMTP

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
My_twilio_number = os.environ["My_twilio_number"]

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def notify_manager(self, text):
        # client = self.client
        # message = client.messages \
        #     .create(
        #     body=text,
        #     from_='+12055741799',
        #     to='+2347064938773'
        # )
        # print(message.sid)
        # print(message.status)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="ezerowoeye@yahoo.com",
                                msg=f"Subject:Update on Flight price\n\n{text}".encode("utf8"))
