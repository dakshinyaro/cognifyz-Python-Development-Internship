# -----------------------------------------
# Project: String Reversal
# Author: Dakshinya A
# Description:
# This program takes a string from the user
# and prints its reverse.
# -----------------------------------------

def reverse_string(text):
    return text[::-1]


def main():
    print("========== String Reversal Program ==========")

    user_input = input("Enter a string: ")

    reversed_text = reverse_string(user_input)

    print("\nOriginal String :", user_input)
    print("Reversed String :", reversed_text)


if __name__ == "__main__":
    main()