import random


def play():
    welcome()
    secret_word = load_secret_word()
    result = game(secret_word)
    show_result(result, secret_word)
    game_over()


def game(secret_word):
    right_letters = init_right_letters(secret_word)
    print(right_letters)

    completely_guessed = False
    hanged = False
    max_attempts = 7
    errors = 0

    while not hanged and not completely_guessed:
        guess_letter = ask_for_a_letter_guess()

        if guess_letter in secret_word:
            mark_right_guess(guess_letter, right_letters, secret_word)
            completely_guessed = "_" not in right_letters
        else:
            errors += 1
            draw_hang(errors)
            hanged = errors == max_attempts
            show_error_message(errors, max_attempts)

        print(right_letters)

    return completely_guessed


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def show_result(completely_guessed, secret_word):
    show_win() if completely_guessed else show_lose(secret_word)


def show_lose(secret_word):
    print("Oops, you got hanged!")
    print(f"The word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def show_win():
    print("Congratulations! You got it right! :)")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def show_error_message(errors, max_attempts):
    print(f"Oops, you missed! More {max_attempts - errors} attempts.")


def mark_right_guess(guess_letter, right_letters, secret_word):
    for index, letter in enumerate(secret_word):
        if letter == guess_letter:
            right_letters[index] = letter


def ask_for_a_letter_guess():
    return input("Pick a letter: ").strip().upper()


def init_right_letters(word):
    return ["_" for _ in word]


def load_secret_word(file_name="words.txt", first_valid_line=0):
    with open(file_name, "r") as words_file:
        words = [word.strip() for word in words_file]
    random_word_index = random.randrange(first_valid_line, len(words))
    secret_word = words[random_word_index].upper()
    return secret_word


def welcome():
    print("******************************")
    print("***** Welcome to Hangman *****")
    print("******************************")


def game_over():
    print("***************************")
    print("******* Game over! ********")
    print("***************************")


if __name__ == "__main__":
    play()
