import requests
import os
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]
print("Welcome to Ezer's flight club\nWe find the best deals and email you")
match_mails = True
# another_user = ""


def add_user():
    user_first_name = input("What is your first name?\n")
    user_last_name = input("What is your last name?\n")
    user_email = input("What is your email?\n")
    user_email_again = input("Type your email again.\n")
    if user_email_again == user_email:
        print("Success, your email has been added to the flight club")
    else:
        print("The email must match")

    new_data = {
        "user": {
            "firstName": user_first_name,
            "lastName": user_last_name,
            "email": user_email
        }
    }
    # response = requests.put(url=f"{SHEETY_ENDPOINT}/2", json=new_data)
    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_data)
    print(response.text)


add_user()
while match_mails:
    another_user = input("Would you like to add another user? \nType Yes/No: ").title()
    if another_user == "Yes":
        add_user()
    else:
        match_mails = False
        print("Thank You")



