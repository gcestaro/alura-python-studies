# all python built-in functions are inside "builtins" package
from builtins import print
import random


def play():
    print("***************************************")
    print("***** Welcome to Guess the Number *****")
    print("***************************************")

    print("Choose the difficulty level:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    print("4 - Very Hard")

    level = int(input("Pick a level number: "))

    if level == 1:
        max_attempts = 20
    elif level == 2:
        max_attempts = 14
    elif level == 3:
        max_attempts = 7
    else:
        max_attempts = 4

    secret_number = round(random.randrange(1, 101))
    current_attempt = 0

    user_points = 1000

    while current_attempt < max_attempts:
        current_attempt += 1
        print(f'Attempt {current_attempt} of {max_attempts}')

        guess_number = int(input("Guess the number: (0 < number =< 100)"))
        print("You guessed ", guess_number)
        if guess_number < 1 or guess_number > 100:
            print("You lost a round! Try a number between 1 and 100.")
            continue

        if secret_number == guess_number:
            print(f"Here we go! You got it right at attempt {current_attempt} and finish with {user_points} points!")
            break
        else:
            print("Nope! Try again...")
            lost_points = round(abs(secret_number - guess_number) / 3)
            user_points -= lost_points
            if guess_number > secret_number:
                print("Your guess is higher!")
            elif guess_number < secret_number:
                print("Your guess is lower!")

    print(f"The number was {secret_number}")
    print("******************************************")
    print("Game over...")


if __name__ == "__main__":
    play()
