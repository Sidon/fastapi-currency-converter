from src.api.utils import currency_conversion


def test_convert_currency():
    conversion = {"from_currency": "USD", "to_currency": "BRL", "amount": 100.0}
    response = currency_conversion(conversion)
    assert response > 0
