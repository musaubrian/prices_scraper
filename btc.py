#!/usr/bin/env python3
"""
gets price of bitcoin in USD
and converts to KES
"""

import requests


def main():
    print("""
            |---------------------------------|
            |        BTC Price checker        |
            |                                 |
            |       Panics if BTC < $ 19K     |
            |                                 |
            |---------------------------------|
            """)
    one_btc = 1
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(api_url)
    json_response = response.json()
    btc = json_response['bpi']["USD"]['rate'].split(',')
    new_price = btc_converter(btc, float(one_btc))
    price_in_usd = f"{int(new_price[0])}{int(new_price[1])}"
    convert_to_kes(int(price_in_usd))


def btc_converter(btc, n):
    """
    gets the price from th json api and stores in an array

    btc[0]: thousands section of the price
    btc[1]: hundreds section of the price
    """
    new_price = []
    new_price.append(float(btc[0]) * n)
    new_price[0] += float(btc[1]) * n // 1000
    new_price.append((float(btc[1]) * n % 1000))
    return new_price


def convert_to_kes(usd: int):
    """
    converts the USD price to KES

    Args::
        usd(str): btc price in USD
    """
    convertion_rate = int(input("Enter current conversion rate(1~1000): "))
    curr_prefix = input("Currency prefix(USD/KES): ")
    usd_to_kes = usd * convertion_rate

    usd_shorthand = usd / 1000
    kes_shorthand = usd_to_kes / 1000000

    print(f"\nUSD {usd}\n 1 BTC = USD {usd_shorthand:.2f}K")
    print(f"{curr_prefix} {usd_to_kes}\n 1 BTC = {curr_prefix} {kes_shorthand:.2f}M")
    print("*"*25)
    if usd < 19000:
        print(f"\nBUY THE DIP!!!")
    elif usd > 19000 and usd < 25000:
        print(f"\nHODLE!!!")



if __name__ == "__main__":
    main()
