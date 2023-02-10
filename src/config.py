import os

from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv("FIXER_API_KEY", "UojpqFHgYZb3EMw2W4v9Gkh05B0kOM2s")
URL_CONVERT = os.getenv("URL_CONVERT", "https://api.apilayer.com/fixer/convert")
URL_4217 = "https://en.wikipedia.org/wiki/ISO_4217"
