import os
import requests
from dotenv import load_dotenv
from fastapi import APIRouter

router = APIRouter()

load_dotenv()


def convert_endpoint(from_currency: str, to_currency: str, amount: float ):
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
    # access_key = os.getenv("FIXER_API_KEY", "UojpqFHgYZb3EMw2W4v9Gkh05B0kOM2s")
    access_key = "UojpqFHgYZb3EMw2W4v9Gkh05B0kOM2s"

    payload = {}
    headers = {
        "apikey": access_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # result = response.text

    if response.status_code == 200:
        # breakpoint()
        return response.json()
    else:
        return {"error": "Conversion failed"}
