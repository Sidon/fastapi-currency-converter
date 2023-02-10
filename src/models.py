from pydantic import BaseModel, constr, conint


class CurrencyConversion(BaseModel):
    from_currency: constr(regex="^[A-Z]{3}$")
    to_currency: constr(regex="^[A-Z]{3}$")
    amount: float
