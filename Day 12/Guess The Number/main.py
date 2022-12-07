from art import logo
import random


def main():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    number_range = [num for num in range(1, 101)]
    # the computer pick
    the_number = random.choice(number_range)

    # avaible attempts
    attempts = choose_difficulty()
    game(the_number, attempts)


# functions that returns user avaible attempts which depends on game difficulty
def choose_difficulty():
    user_difficulty_choice = input(
        "Choose a difficulty. Type 'easy' or 'hard': ")
    if user_difficulty_choice == 'easy':
        return 10
    elif user_difficulty_choice == 'hard':
        return 5
    else:
        print('You chose god mode difficulty level.')
        return 1


def game(the_number, attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    # take user guess which must be a number
    while True:
        user_guess = input('Make a guess: ')
        try:
            user_guess = int(user_guess)
            break
        except:
            print('Your guess must be a number!')

    if user_guess == the_number:
        print("You guess the correct number! You are reading in my mind!")
        return 0
    elif user_guess > the_number:
        print('Too high')
    elif user_guess < the_number:
        print('Too low')
    if attempts == 1:
        print(
            "You've run out of attempts. You can do it next time but you lost this game!"
        )
        return 0
    else:
        return game(the_number, attempts - 1)


main()