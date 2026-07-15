# --------------------------------------------
# Project : Calculator
# Author  : Dakshinya A
# Description:
# A simple menu-driven calculator that
# performs basic arithmetic operations.
# --------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


while True:

    print("\n" + "=" * 50)
    print("           SIMPLE CALCULATOR")
    print("=" * 50)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using the Calculator.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"\nResult = {add(num1, num2)}")

        elif choice == "2":
            print(f"\nResult = {subtract(num1, num2)}")

        elif choice == "3":
            print(f"\nResult = {multiply(num1, num2)}")

        elif choice == "4":
            result = divide(num1, num2)

            if result is None:
                print("\nError! Division by zero is not allowed.")
            else:
                print(f"\nResult = {result}")

    except ValueError:
        print("\nPlease enter valid numeric values.")