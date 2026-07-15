# --------------------------------------------
# Project : Palindrome Checker
# Author  : Dakshinya A
# Description:
# This program checks whether a word or
# sentence is a palindrome.
# --------------------------------------------

def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()

    return cleaned_text == cleaned_text[::-1]


def main():

    print("=" * 50)
    print("          PALINDROME CHECKER")
    print("=" * 50)

    while True:

        text = input("\nEnter a word or sentence: ")

        if is_palindrome(text):
            print("\n✅ It is a Palindrome.")
        else:
            print("\n❌ It is NOT a Palindrome.")

        choice = input("\nDo you want to check another? (Y/N): ").lower()

        if choice != "y":
            print("\nThank you for using the Palindrome Checker.")
            break


if __name__ == "__main__":
    main()