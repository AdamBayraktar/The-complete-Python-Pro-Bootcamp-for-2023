import random
from art import logo
import os



def main():
    # ask the user if he wants to play
    while True:
        play_or_quit = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_or_quit == 'y':
            os.system('cls')
            break
        elif play_or_quit == 'n':
            print('Thank you for your time. Have a nice day my friend!')
            os._exit()
        print('Incorrect input.')

    # prints logo
    print(logo)

    user_cards = []
    computer_cards = []

    # add 2 cards to each decks
    for card in range(2):
        user_cards.append(take_card())
        computer_cards.append(take_card())

    # check if there is a blackjack
    blackjack(user_cards, computer_cards)
    computer_cards = computer_final_deck(computer_cards)

    # loop that goes untill someone wins
    while True:
        first_round(user_cards, computer_cards)
        # check if user went over
        if sum(user_cards) > 21:
            final_round(user_cards, computer_cards)
            print("You went over \U0001F480")
            main()
        # ask if user want to take a card or not
        if another_game():
            user_cards.append(take_card())
        else:
            final_round(user_cards, computer_cards)
            final_result(user_cards, computer_cards)

    # win with blackjack


# randomly returns card from deck
def take_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def computer_final_deck(comp_deck):
    score = sum(comp_deck)
    # check score if is higher than 21
    # if yes look for ACE to change value from 11 to 1
    if score > 21 and 11 in comp_deck:
        comp_deck.remove(11)
        comp_deck.append(1)
        return computer_final_deck(comp_deck)
    # if score higher 15 return completed deck
    elif score > 15:
        return comp_deck
    # add card if value is lower than 15
    else:
        comp_deck.append(take_card())
        return computer_final_deck(comp_deck)


# print first round texts
def first_round(user_deck, comp_deck):
    print(f"Your cards: {user_deck}, current score {sum(user_deck)}")
    print(f"Computer's first card: {comp_deck[0]}")


# print final text
def final_round(user_deck, comp_deck):
    print(f"Your final hand: {user_deck}, final score {sum(user_deck)}")
    print(
        f"Computer's final hand: {comp_deck[0]}, final score {sum(comp_deck)}")


# function that checks if there is a blackjack
def blackjack(user_deck, comp_deck):
    # user has Blackjack
    if sum(user_deck) == 21:
        first_round(user_deck, comp_deck)
        final_round(user_deck, comp_deck)
        print("You win! You have Blackjack \U0001F911")
        main()
    # comp has Blackjack
    elif sum(comp_deck) == 21:
        first_round(user_deck, comp_deck)
        final_round(user_deck, comp_deck)
        print("You lost! Opponent has Blackjack \U0001F631")
        main()


# return True if user wants another card
def another_game():
    user_input = input('Type "y" to get another card, type "n" to pass: ')
    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    print('Invalid input. Try again.')
    return another_game()


# compare hands and show the result
def final_result(user_deck, comp_deck):
    user_deck = sum(user_deck)
    comp_deck = sum(comp_deck)
    if user_deck > 21:
        print("You lose because you went over! \U0001F4A9")
    elif comp_deck > 21:
        print("Opponent went over. You win!\U0001F478")
    elif user_deck == comp_deck:
        print("It is a draw! \U0001F91D")
    elif user_deck > comp_deck:
        print("You win!\U0001F947\U0001F3C6")
    else:
        print("You lose because your hand is weaker! \U0001F940")
    main()


main()
