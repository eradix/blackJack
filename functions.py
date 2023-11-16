import random
import os
from art import logo

"""List of cards"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clean_screen():
    '''clear the console screen'''
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def deal_card():
    """deal a card and pick 1 randomly"""
    return random.choice(cards)

def calculate_score(cards):
  """calculate all cards"""
  if sum(cards) == 21 and len(cards) == 2:
      return 0
  if sum(cards) > 21 and 11 in cards:
      cards[cards.index(11)] = 1
      return sum(cards)
  return sum(cards)

def compare(user_score, computer_score):
    """compare user and computer cards"""
    if user_score == computer_score:
        print("oops. Its a draw.")
    elif computer_score == 0:
        print("Blackjack! You lose.")
    elif user_score == 0:
        print("Blackjack! You win!")
    elif user_score > 21:
        print("You went over. You lose.")
    elif  computer_score > 21:
        print("Computer went over. You win!")
    elif user_score > computer_score:
        print("You got a higher score. You win!")
    else:
        print("You got a lower score. You lose.")


def play_game():
    """play black jack game"""
    
    # game logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # deal 2 cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)

    while not is_game_over:

        user_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # validate that user must input correctly
            while True:
                user_desc = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if user_desc not in ['y', 'n']:
                    print('Invalid input. Please try again.')
                elif user_desc == 'y':
                    user_cards.append(deal_card())
                    break
                else:
                    is_game_over = True
                    break

    while computer_score != 0 and computer_score  < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print("\nFINAL DECK")
    print(f"You cards: {user_cards} = {user_score}")
    print(f"Computer cards: {computer_cards} = {computer_score}")

    compare(user_score=user_score, computer_score=computer_score)


