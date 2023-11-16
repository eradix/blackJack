from functions import clean_screen, play_game

if __name__ == '__main__':
    # execute game
    run_game = True
    while run_game:
        user_to_play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_to_play not in ['y','n']:
            print('Invalid input.')
        elif user_to_play == 'n':
            print("Program Terminated")
            run_game = False
        else:
            clean_screen()
            play_game()
