# --------------------------------------------
# Project : Data Visualization
# Author  : Dakshinya A
# Description:
# Reads sales data from a CSV file and
# displays a line chart using Matplotlib.
# --------------------------------------------

import csv
import matplotlib.pyplot as plt

months = []
sales = []

try:
    with open("dataset.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            months.append(row["Month"])
            sales.append(int(row["Sales"]))

    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker="o")

    plt.title("Monthly Sales Report")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: dataset.csv not found.")