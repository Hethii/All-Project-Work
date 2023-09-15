# a tip calculator
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percent_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
percent_number = (int(percent_tip) / 100)
tip_value = percent_number * total_bill
added_tip = (total_bill) + tip_value
spliting_people = input("How many people to split the bill? ")

spliting_people2int = int(spliting_people)

each_to_pay = round(added_tip / spliting_people2int, 2)

result = f"Each person should pay: ${each_to_pay}"
print(result)