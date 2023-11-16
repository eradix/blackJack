from functions import clean_screen, play_game

if __name__ == '__main__':
    # execute game
    while input("\nDo you want to play a game of Blackjack again? Type 'y' or 'n': ").lower() == 'y':
        clean_screen()
        play_game()
