# --------------------------------------------
# Project : Number Guesser
# Author  : Dakshinya A
# Description:
# The computer guesses the number that
# the user is thinking of.
# --------------------------------------------

print("=" * 50)
print("           NUMBER GUESSER")
print("=" * 50)

print("\nThink of a number between 1 and 100.")
input("Press Enter when you're ready...")

low = 1
high = 100
attempts = 0

while low <= high:

    guess = (low + high) // 2
    attempts += 1

    print(f"\nIs your number {guess}?")
    print("H = Too High")
    print("L = Too Low")
    print("C = Correct")

    choice = input("Enter your choice (H/L/C): ").upper()

    if choice == "C":
        print(f"\n🎉 I guessed your number in {attempts} attempt(s)!")
        break

    elif choice == "H":
        high = guess - 1

    elif choice == "L":
        low = guess + 1

    else:
        print("Invalid input! Please enter H, L, or C.")