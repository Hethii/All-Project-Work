# Building a Ceaser Cipher Game:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                 'x', 'y', 'z']

# Credible Use of function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #to process decoding without long codes:
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #To makde sure numbers/symbols/spaces gets printed too
    if char not in alphabet: 
      end_text += char
    elif char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#this logo is from ascii.
from art import logo
print(logo)

#while loop to keep the game running but to end when if_yes = False
if_yes =True
while if_yes:
  # To make sure its 'encode' or 'decode' the user input:
  correct_direction = True
  while correct_direction:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
      correct_direction = False
    else:
      print("Please input 'Encode' or 'Decode' only\n")
    
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#if shift input is higher than 26:
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
  start_or_end= input("Do you want to go again? 'Yes' to go again and 'No' to End:\n").lower()
  # To end the game:
  if start_or_end == 'no':
    if_yes = False
    print("Cipher Over")
