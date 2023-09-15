# Day 4: Rock, Paper, Scissors game
# my code for this:

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
x =input('Type Start to begin the Game or Type Stop to End the Game ')

while x == "Start":
    choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    
    computer_guess = random.randint(0, 2)
    if choose == 0:
        choose = rock
        print(rock)
        if computer_guess == 0:
            print("computer choose:")
            print(rock)
            print("You Draw")
        elif computer_guess == 1:
            print("computer choose:")
            print(paper)
            print("You loss")
        else:
            print("computer choose:")
            print(scissors)
            print("You Win")
        
    elif choose == 1:
        choose = paper
        print(paper)
        if computer_guess == 0:
            print("computer choose:")
            print(rock)
            print("You win")
        elif computer_guess == 1:
            print("computer choose:")
            print(paper)
            print("You draw")
        else:
            print("computer choose:")
            print(scissors)
            print("You lose") 
    
    elif choose == 2:
        choose = scissors
        print(scissors)
        if computer_guess == 0:
            print("computer choose:")
            print(rock)
            print("You lose")
        elif computer_guess == 1:
            print("computer choose:")
            print(paper)
            print("You win")
        else:
            print("computer choose:")
            print(scissors)
            print("You draw")
    else:
        print(f"{choose} is not an option. Pick either 0, 1 or 2")
        continue

else:
  print('Game has ended. thank you for playing')


# Miss Angela Yu Code (after debugging)
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    
    
    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")