# DID THIS WITHOUT USING ANY HINTS


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

the_beginning = True
while the_beginning:
  start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if start == "y":
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    computer_choice = []
    user_choice = []
    
    
    def result():
      print(f"    Your cards: {user_choice}, current score: {user_result}")
      computer_first = computer_choice[0]
      print(f"    Computer's first card: {computer_first}")
      

    def computer_guess(card):
      computer_total = 0
      run_through = [0,1]
      for running in run_through:
        computer= random.choice(cards)
        computer_choice.append(computer)

        computer_total += computer_choice[running]
      return computer_total

    
    def user_guess(cards):
      user_total = 0 

      run_through = [0,1]
      for running in run_through:
        user_pick = random.choice(cards)
        user_choice.append(user_pick)
      
        user_total += user_choice[running]
    
      return user_total
      
    user_result = user_guess(cards)
    computer_result = computer_guess(cards)
    
    result()
    if sum(user_choice) == 21 and sum(computer_choice) != 21:
      print(f"    Your final hand: {user_choice}, final score: {user_result}")
      print(f"    Computer's final hand: {computer_choice}, final score: {computer_result}")
      any_jubs = [0,1]
      best_jubilation = random.choice(any_jubs)
      if best_jubilation == 0:
        print("You have a blackjack 🤯. You win")
      else:
        print("Win with a Blackjack 😎")
    elif sum(computer_choice) == 21 and sum(user_choice) != 21:
      print(f"    Your final hand: {user_choice}, final score: {user_result}")
      print(f"    Computer's final hand: {computer_choice}, final score: {computer_result}")
      print("Opponent has a blackjack. You lose😭")
    else:
      is_true = True
      while is_true:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_continue == "n":
          is_true = False
        elif should_continue == "y":
          user_pick = random.choice(cards)
          user_choice.append(user_pick)
          if 11 in user_choice and sum(user_choice) > 21:
            user_pick = 1
            user_choice.remove(11)
            user_choice.append(1)
          
            
          # print(user_choice)
          user_index = user_choice.index(user_pick)
          user_result += user_choice[user_index]
     
        is_comp_again = True
        while is_comp_again:
          if computer_result <= 17:
            computer_answer = ["y", "y", "y", "n"]
            computer_again = random.choice(computer_answer)
    
            if computer_again == "y":
              computer= random.choice(cards)
              computer_choice.append(computer)
              if 11 in computer_choice and sum(computer_choice) > 21:
                computer = 1
                computer_choice.remove(11)
                computer_choice.append(1)
              computer_index = computer_choice.index(computer)
              computer_result += computer_choice[computer_index]
            else:
              computer_result = computer_result
              is_comp_again = False          
          elif computer_result > 17:
            is_comp_again= False
          
        
        result()
  
      print(f"    Your final hand: {user_choice}, final score: {user_result}")
      print(f"    Computer's final hand: {computer_choice}, final score: {computer_result}")

      if user_result > computer_result and user_result <= 21:
        print("You Win! 😃")
      elif computer_result > user_result and computer_result <= 21:
        print("You lose. 😤")  
      elif user_result > 21 and computer_result > user_result:
        print("Opponent went over. You win 😁")
      elif computer_result > 21 and user_result > computer_result:
        print("You went over. You lose 😭")
      elif user_result < 21 and computer_result > 21:
        print("Opponent went over. You win 😁")
      elif computer_result < 21 and user_result > 21:
        print("You went over. You lose 😭")
      else:
        print("You Draw 🙃")
  
  else:
    the_beginning= False