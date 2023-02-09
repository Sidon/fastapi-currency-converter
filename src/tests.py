from src.api import endpoints


def test_convert_currency():
    conversion = {"from_currency": "USD", "to_currency": "BRL", "amount": 100.0}
    response = endpoints(conversion)
    assert response > 0
