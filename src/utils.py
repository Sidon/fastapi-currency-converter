import requests


def convert_currency(base, symbol, amount):
    response = requests.get(f"http://data.fixer.io/api/latest?access_key=YOUR_ACCESS_KEY&base={base}&symbols={symbol}")
    data = response.json()
    exchange_rate = data["rates"][symbol]
    return amount * exchange_rate
