# -----------------------------------------
# Project: Temperature Converter
# Author: Dakshinya A
# Description:
# This program converts temperature between
# Celsius, Fahrenheit, and Kelvin.
# -----------------------------------------

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def main():
    print("=" * 45)
    print("        Temperature Converter")
    print("=" * 45)

    print("\nSelect Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"\nResult: {celsius:.2f}°C = {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"\nResult: {fahrenheit:.2f}°F = {celsius:.2f}°C")

    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"\nResult: {celsius:.2f}°C = {kelvin:.2f} K")

    elif choice == "4":
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"\nResult: {kelvin:.2f} K = {celsius:.2f}°C")

    else:
        print("\nInvalid choice! Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()