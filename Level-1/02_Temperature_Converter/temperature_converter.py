# --------------------------------------------
# Project : Temperature Converter
# Author  : Dakshinya A
# Description:
# A menu-driven temperature converter that
# converts between Celsius, Fahrenheit,
# and Kelvin.
# --------------------------------------------

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


while True:

    print("\n" + "=" * 50)
    print("        TEMPERATURE CONVERTER")
    print("=" * 50)

    print("1. Celsius ➜ Fahrenheit")
    print("2. Fahrenheit ➜ Celsius")
    print("3. Celsius ➜ Kelvin")
    print("4. Kelvin ➜ Celsius")
    print("5. Fahrenheit ➜ Kelvin")
    print("6. Kelvin ➜ Fahrenheit")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "7":
        print("\nThank you for using the Temperature Converter!")
        break

    try:
        temperature = float(input("Enter temperature value: "))

        if choice == "1":
            result = celsius_to_fahrenheit(temperature)
            print(f"\n{temperature:.2f} °C = {result:.2f} °F")

        elif choice == "2":
            result = fahrenheit_to_celsius(temperature)
            print(f"\n{temperature:.2f} °F = {result:.2f} °C")

        elif choice == "3":
            result = celsius_to_kelvin(temperature)
            print(f"\n{temperature:.2f} °C = {result:.2f} K")

        elif choice == "4":
            result = kelvin_to_celsius(temperature)
            print(f"\n{temperature:.2f} K = {result:.2f} °C")

        elif choice == "5":
            result = fahrenheit_to_kelvin(temperature)
            print(f"\n{temperature:.2f} °F = {result:.2f} K")

        elif choice == "6":
            result = kelvin_to_fahrenheit(temperature)
            print(f"\n{temperature:.2f} K = {result:.2f} °F")

        else:
            print("\nInvalid choice! Please select between 1 and 7.")

    except ValueError:
        print("\nPlease enter a valid numeric value.")