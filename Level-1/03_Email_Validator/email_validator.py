# --------------------------------------------
# Project : Email Validator
# Author  : Dakshinya A
# Description:
# This program validates an email address
# using Regular Expressions (Regex).
# --------------------------------------------

import re


def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if re.fullmatch(pattern, email):
        return True
    return False


def main():

    print("=" * 50)
    print("            EMAIL VALIDATOR")
    print("=" * 50)

    while True:

        email = input("\nEnter an email address: ")

        if validate_email(email):
            print("\n✅ Valid Email Address")
        else:
            print("\n❌ Invalid Email Address")

        choice = input("\nDo you want to check another email? (Y/N): ").lower()

        if choice != "y":
            print("\nThank you for using Email Validator.")
            break


if __name__ == "__main__":
    main()