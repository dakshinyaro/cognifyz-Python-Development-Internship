# --------------------------------------------
# Project : Guessing Game
# Author  : Dakshinya A
# Description:
# A number guessing game where the user
# tries to guess a randomly generated number.
# --------------------------------------------

import random

print("=" * 50)
print("          NUMBER GUESSING GAME")
print("=" * 50)

while True:

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:

        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"\n🎉 Congratulations!")
                print(f"You guessed the number in {attempts} attempt(s).")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("\nDo you want to play again? (Y/N): ").lower()

    if play_again != "y":
        print("\nThank you for playing!")
        break