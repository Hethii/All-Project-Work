# day 5-- Build a password generator
# MY CODE
#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# alphabet =""
# for number in range(1, nr_letters + 1):
#   list_pick= random.randint(1, 51)
#   alphabet += letters[list_pick]
# # print(alphabet)

# symbol = ""
# for character in range(1, nr_symbols + 1):
#   list_symbol_pick = random.randint(1, 8)
#   symbol += symbols[list_symbol_pick]
# # print(symbol)

# digit = ""
# for number in range(1, nr_numbers + 1):
#   list_number_pick =  random.randint(1, 9)
#   digit += numbers[list_number_pick]
# # print(digit)

# password = alphabet + digit + symbol
# print(password)

# This will create a password.

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Trying to figure out how to randomize the created password abov. Couldnt finish up

# randomized_password=""

# addition = nr_letters + nr_numbers + nr_symbols
# d = 1
# for order in range(0, addition + 1):
  
#   hello = random.randint(0, addition - 1)
  
#   print(hello)
#   randomized_password += password[hello]
# print(randomized_password)

# randomized_password=""

# addition = nr_letters + nr_numbers + nr_symbols
# d = 0
# e = []
# f=""
# while d < addition:
#   hello = random.randint(0, addition - 1)
#   f += str(hello)
  
#   for y in z:
#     if y == hello:
#       e.append(y)
#     elif hello != e:
#       randomized_password += password[hello]
#   d += 1

# print(randomized_password)


#Angela Yu code:
# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
              'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level