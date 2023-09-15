import random
from game_data import data
from art import logo, vs
# from replit import clear

choice = ""
choice2 = random.choice(data)
first = ""
second = ""

def printchoice(choice, choice2, current_score):
#   clear()
  print(logo)
  if current_score >= 1:
    print(f"You're right! Current score: {current_score}.")
  else:
    current_score = 0
  print(f"Compare A: {choice['name']} , a {choice['description']}, from {choice['country']}.")
  print(vs)
  print(f"Against B: {choice2['name']} , a {choice2['description']}, from {choice2['country']}.")

is_true = True
def game(first, second, choice, choice2):
  is_true = True
  current_score = 0
  while is_true:
    play_again = input("Do you want to play? y or n: ").lower()
    # clear()
    if play_again == 'y': 
      secondtime = True
      while secondtime:
        choice = choice2
        choice2 = random.choice(data)
        while choice == choice2:
          choice2 = random.choice(data)
        first = choice['follower_count']
        second = choice2['follower_count']

        printchoice(choice, choice2, current_score)
        # print(first)
        # print(second)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == "a"  and first > second:
          current_score += 1
        elif answer == "b" and second > first:
          current_score += 1
        else:
        #   clear()
          print(logo)
          print(f"Sorry, well, that's wrong. Final score: {current_score}.")
          secondtime = False
    else:
      is_true = False

game(first, second, choice, choice2)