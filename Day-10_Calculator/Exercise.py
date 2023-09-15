# 1 create a way for check if what month will be in a leap year or not leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    """My Code result"""
    if month > 12 or month < 1:
        return("Invalid Input")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    the_days = month_days[month - 1]
    if is_leap(year):
        the_days += 1
        return the_days
    elif is_leap(year) == False:
        return the_days
    
    # if is_leap(year) and month == 2:
    #     return 29
    # return(month_days[month - 1])



#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# DOCSTRINGS:
# they are for adding what functions does.



def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : "add",
  "-" : "substract",
  "*" : "multiply",
  "/" : "divide"
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
for symbols in operations:
  print(symbols)
operand = input("Pick an operation from the line above: ")
# if operand == "+":
#   answer = add(number1, number2)
# elif operand == "-":
#   answer =  substract(number1, number2)
# elif operand == "*":
#   answer =  multiply(number1, number2)
# elif operand == "/":
# #   answer =  divide(number1, number2)
# calculation_symbol = operations[operand]
# print(calculation_symbol)
# answer = calculation_symbol(number1, number2)

# print(f"{number1} {operand} {number2} = {answer}")

operation_symbol = input("Pick an operation: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")