import random
from art import logo
print(logo)

the_start = True
while the_start:
  start= input("Type 'y' to play or 'n' to stop: ")
  if start == "y":
    the_answer = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    trials = [10, 5]
    
    def guessing_game(index, the_answer):
      """This runs the game function"""
      is_true = True
      number_of_trials = 0
      while is_true:
      # print(the_answer)
        if index == 0:
          print("You've run out of guesses, you lose.")
          is_true = False
        else:
          if index > 0 and number_of_trials > 0:
            print("Guess again")
          print(f"You have {index} attempts remaining to guess the number.")
          the_guess = int(input("Make a guess: "))
          number_of_trials = 1
          if the_guess == the_answer:
            print(f"You got it! The answer was {the_answer}.")
            is_true = False
          elif the_guess < the_answer:
            print("Too Low")
            index -= 1
          elif the_guess > the_answer:
            print("Too High")
            index -= 1
     
    # print(the_answer)
    if difficulty == "easy":
      index = trials[0]
      # print(index)
      guessing_game(index, the_answer)
    else:
      index = trials[1]
      # print(index)
      guessing_game(index, the_answer)
  else:
    the_start = False