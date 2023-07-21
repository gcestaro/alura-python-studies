import guess_the_number
import hangman


def choose_game():
    print("*****************************")
    print("***** Choose your game! *****")
    print("*****************************")

    print("Choose the game:")
    print("1 - Hangman")
    print("2 - Guess the number")

    game_choose = int(input("Pick a number: "))

    if game_choose == 1:
        hangman.play()
    elif game_choose == 2:
        guess_the_number.play()


if __name__ == "__main__":
    choose_game()
