# --------------------------------------------
# Project : File Word Counter
# Author  : Dakshinya A
# Description:
# This program reads a text file and counts
# the number of lines, words, and characters.
# --------------------------------------------

import os


def count_file_contents(filename):

    if not os.path.exists(filename):
        print("\nError: File not found.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("\n========== FILE ANALYSIS ==========")
    print(f"File Name      : {filename}")
    print(f"Total Lines    : {len(lines)}")
    print(f"Total Words    : {len(words)}")
    print(f"Total Characters : {characters}")
    print("===================================")


print("=" * 50)
print("          FILE WORD COUNTER")
print("=" * 50)

while True:

    filename = input("\nEnter the file name (Example: sample.txt): ")

    count_file_contents(filename)

    choice = input("\nAnalyze another file? (Y/N): ").lower()

    if choice != "y":
        print("\nThank you for using File Word Counter.")
        break