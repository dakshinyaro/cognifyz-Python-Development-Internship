# --------------------------------------------
# Project : Fibonacci Generator
# Author  : Dakshinya A
# Description:
# This program generates the Fibonacci
# sequence based on the number of terms
# entered by the user.
# --------------------------------------------

def fibonacci(n):

    sequence = []

    first = 0
    second = 1

    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    return sequence


print("=" * 55)
print("          FIBONACCI GENERATOR")
print("=" * 55)

while True:

    try:
        terms = int(input("\nEnter the number of terms: "))

        if terms <= 0:
            print("Please enter a positive number.")
            continue

        result = fibonacci(terms)

        print("\nFibonacci Sequence:")
        print(*result)

    except ValueError:
        print("Please enter a valid integer.")

    choice = input("\nGenerate another sequence? (Y/N): ").lower()

    if choice != "y":
        print("\nThank you for using Fibonacci Generator.")
        break