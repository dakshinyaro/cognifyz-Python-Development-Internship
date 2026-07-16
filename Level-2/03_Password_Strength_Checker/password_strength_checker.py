# --------------------------------------------
# Project : Password Strength Checker
# Author  : Dakshinya A
# Description:
# This program checks the strength of a
# password based on security rules.
# --------------------------------------------

import re


def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Very Strong 💪"

    elif score == 4:
        return "Strong ✅"

    elif score == 3:
        return "Medium ⚠️"

    elif score == 2:
        return "Weak ❌"

    else:
        return "Very Weak 🚫"


print("=" * 55)
print("          PASSWORD STRENGTH CHECKER")
print("=" * 55)

while True:

    password = input("\nEnter your password: ")

    strength = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    print("\nPassword Rules:")
    print("✔ Minimum 8 characters")
    print("✔ At least one uppercase letter")
    print("✔ At least one lowercase letter")
    print("✔ At least one digit")
    print("✔ At least one special character")

    choice = input("\nCheck another password? (Y/N): ").lower()

    if choice != "y":
        print("\nThank you for using Password Strength Checker.")
        break