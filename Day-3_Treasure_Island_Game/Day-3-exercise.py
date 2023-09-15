# Day 3 exercise
# a tip calculator
# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill? $"))
# percent_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
# percent_number = (int(percent_tip) / 100)
# tip_value = percent_number * total_bill
# added_tip = (total_bill) + tip_value
# spliting_people = input("How many people to split the bill? ")

# spliting_people2int = int(spliting_people)

# each_to_pay = round(added_tip / spliting_people2int, 2)

# result = f"Each person should pay: ${each_to_pay}"
# print(result)

# Day 3.
# To calculate BMI (Body Mass Index)
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# BMI = round(weight / (height ** 2))

# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI <25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI  < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

# Day 4.
# To calculate Leap year
# year = int(input("Which year do you want to check? "))

# This to help understand.
# print(f"by 4= {year / 4}")
# print(f"by 100= {year / 100}")
# print(f"by 400= {year / 400}")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")    

# Day 3: build a pizza order program

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill =+ 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# Day 3: Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name3 = name1 + name2
lowercase_case = name3.lower()
times_in = lowercase_case.count("t")
times_in2 = lowercase_case.count("r")
times_in3 = lowercase_case.count("u")
times_in4 = lowercase_case.count("e")

total_true = str(times_in + times_in2 + times_in3 + times_in4)

love_in = lowercase_case.count("l")
love_in2 = lowercase_case.count("o")
love_in3 = lowercase_case.count("v")
love_in4 = lowercase_case.count("e")

total_love= str(love_in + love_in2 + love_in3 + love_in4)

Total =int(total_true + total_love)

if (Total < 10 or Total > 90):
    print(f"Your score is {Total}, you go together like coke and mentos.")
elif (Total >= 40) and (Total <= 50):
    print(f"Your score is {Total}, you are alright together.")
else:
    print(f"Your score is {Total}")