import random
player = input("Please input your name. ")
computer_choice = random.randint(0,10)

def start_game():
  print(f"Welcome to the game.{player}")
  count_of_player_choice = 0
  while True:
    player_choice = input(f"Please seclect a number from 1-10.{player} ")
    count_of_player_choice +=1
    try:
      player_choice_int = int(player_choice)
      if player_choice_int > 10:
        raise ValueError(f"There is an Error.Please enter number from 1-10.Please try again ")
    except ValueError as err:
      print(f"{err}")
    else:
      if player_choice_int > computer_choice:
        print("it is lower")
      elif player_choice_int < computer_choice:
        print("It is higher")
        continue 
      elif player_choice_int == computer_choice:
        print("Got it")
        print(f"There are {count_of_player_choice} attempts you have made.")
        break
      
start_game()
