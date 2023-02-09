from pydantic import BaseModel


class CurrencyConversion(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
