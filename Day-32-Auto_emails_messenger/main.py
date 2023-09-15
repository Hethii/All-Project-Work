##################### Extra Hard Starting Project ######################
import random
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas

# 1: Activate SMTP

MY_EMAIL = ""
MY_PASSWORD = ""

birthday_letters = []


def letter_list():
    global birthday_letters
    with open("letter_templates/letter_1.txt") as first_letter:
        first_list = first_letter.read()
        # print(first_list)
        birthday_letters.append(first_list)

    with open("letter_templates/letter_2.txt") as second_letter:
        second_list = second_letter.read()
        # print(second_list)
        birthday_letters.append(second_list)

    with open("letter_templates/letter_2.txt") as third_letter:
        third_list = third_letter.read()
        # print(third_list)
        birthday_letters.append(third_list)


# 2: Use datatime
now = dt.datetime.now()
day = now.day
month = now.month
# print(day)
# print(month)

# 4: Convert csv file for use
data = pandas.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient="records")
# print(birthday_list)

all_names = data["name"].to_list()
all_email = data["email"].to_list()
all_month = data["month"].to_list()
all_day = data["day"].to_list()
# birthday_name = random.choice(all_names)

if day in all_day:
    day_index = all_day.index(day)
    if month == all_month[day_index]:
        letter_list()
        birthday_wish = random.choice(birthday_letters)
        # print(birthday_wish)
        completed_letter = birthday_wish.replace("[NAME]", f"{all_names[day_index]}")
        # print(completed_letter)
        # print(all_names[month_index])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="ezerowoeye@yahoo.com",
                                msg=f"Subject:Happy Birthday! {all_names[day_index]}\n\n{completed_letter}"
                                )
        # print(f"Happy Birthday! {all_names[day_index]}\n\n{completed_letter}")
