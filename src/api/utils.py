import requests
from fastapi import APIRouter
from ..config import ACCESS_KEY, URL_CONVERT

router = APIRouter()


def currency_conversion(from_currency: str, to_currency: str, amount: float):
    url = f"{URL_CONVERT}?to={to_currency}&from={from_currency}&amount={amount}"

    payload = {}
    headers = {"apikey": ACCESS_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Conversion failed"}
