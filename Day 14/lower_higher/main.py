from game_data import data
from art import logo, vs
import random
import os



def main(score=0):
  # function that picks randomly two objects to compare
  # by default score is 0, if score higher than 0 is passed then prints additional information
  # a_b holds values of object as a dict that are compared (in this case it is number of followers)
  a_b = introduction_to_game(data, score)
  # user_guess takes user input and return win or lose which depends of user choice
  user_guess(a_b, score)



def introduction_to_game(list_of_data_to_compare, score=0):
  """The input must be list that contains dictionary of objects to compare"""
  print(logo)
  if score > 0:
    print(f"You are right! Current score: {score}")
  number_of_object = len(list_of_data_to_compare)
  # index of first object to compare
  object_a_index = list_of_data_to_compare[random.randint(0, number_of_object - 1)]
  # index of second object which can't be the same as first objject
  while True:
    object_b_index = list_of_data_to_compare[random.randint(0, number_of_object - 1)]
    if object_b_index != object_a_index:
      break
  print(f"Compare A: {object_a_index['name']}, {object_a_index['description']}, from {object_a_index['country']}.")
  print(vs)
  print(f"Against B: {object_b_index['name']}, {object_b_index['description']}, from {object_b_index['country']}.")
  return {'A':object_a_index['follower_count'], 'B':object_b_index['follower_count']}



def user_guess(a_b_values, score=0):
  while True:
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
      # if result is negative it means that user guesed incorectlly 
      result = a_b_values[choice] - a_b_values['B']
      if result > 0:
        clear_terminal()
        main(score + 1)
        break
      else:
        user_lost(score)
        break
    elif choice == 'B':
      # if result is negative it means that user guesed incorectlly 
      result = a_b_values[choice] - a_b_values['A']
      if result > 0:
        clear_terminal()
        main(score + 1)
        break
      else:
        user_lost(score)
        break
        


def user_lost(score):
  clear_terminal()
  print(logo)
  print(f"Sorry, that's wrong. Final score: {score}")
  quit_or_continue = input("Type 'y' if you want to continue or anything else to quit game: ")
  if quit_or_continue == 'y':
    clear_terminal()
    main()
  else:
    print("Thanks for the game!. Good bye Friend \U0001F601")



# clears terminal in windows or linux systems
def clear_terminal():
  try:
    os.system('clear')
  except:
    os.system('cls')


    
main()