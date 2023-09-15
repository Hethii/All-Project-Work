# tslznhtmjkfqckzg
import smtplib
import random
import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)

date_of_birth = dt.datetime(year=1998, month=4, day=27)
print(date_of_birth)
# MY_EMAIL = "ezerpeniel@gmail.com"
# MY_PASSWORD = "tslznhtmjkfqckzg"
#
# if day_of_week == 0:
#     with open("quotes.txt") as text_data:
#         all_quotes = text_data.readlines()
#     quote = random.choice(all_quotes)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs="ezerowoeye@yahoo.com",
#                             msg=f"Subject:Hello, Monday Motivations\n\n{quote}")
#




