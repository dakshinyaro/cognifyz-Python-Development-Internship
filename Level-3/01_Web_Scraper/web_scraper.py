# --------------------------------------------
# Project : Web Scraper
# Author  : Dakshinya A
# Description:
# This program downloads a webpage,
# extracts all H2 headings, and saves
# them into a text file.
# --------------------------------------------

import requests
from bs4 import BeautifulSoup


def scrape_headings(url):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        headings = soup.find_all("h2")

        if not headings:
            print("\nNo H2 headings found.")
            return

        with open("headings.txt", "w", encoding="utf-8") as file:

            for index, heading in enumerate(headings, start=1):

                text = heading.get_text(strip=True)

                print(f"{index}. {text}")

                file.write(f"{index}. {text}\n")

        print("\nHeadings have been saved to headings.txt")

    except requests.exceptions.RequestException as error:
        print(f"\nError: {error}")


print("=" * 55)
print("             WEB SCRAPER")
print("=" * 55)

website = input("\nEnter Website URL: ")

scrape_headings(website)