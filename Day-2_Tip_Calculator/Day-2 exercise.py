# Day-2_Tip_Calculator exercise
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")
age2int = (90 - int(age))
days = age2int * 365
weeks = age2int * 52
months = age2int * 12
result = f"You have {days} days, {weeks} weeks, and {months} months left"
print(result)
# print(f"You have {days} days, {weeks} weeks, and {months} months left")