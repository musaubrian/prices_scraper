#!/usr/bin/env python3
"""
scrapes for fuel prices from
www.globalpetrolprices.com/Kenya/
"""

from regex import W
import requests
from bs4 import BeautifulSoup


url = "https://www.globalpetrolprices.com/Kenya/"


def scrape_for_prices(mkt_url: str):
    req = requests.get(url=mkt_url)

    soup = BeautifulSoup(req.content, "html.parser")
    fuel_price_section = soup.find("div", id="graphPageLeft")

    for table_data in fuel_price_section.find_all('tr'):
        print()
        for data in table_data.find_all('td'):
            clean_data = data.text.strip()
            print(clean_data)


if __name__ == "__main__":
    scrape_for_prices(url)
