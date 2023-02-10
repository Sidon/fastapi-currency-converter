from src.api.utils import currency_conversion
import unittest


class CurrencyConversionTest(unittest.TestCase):
    def test_currency_conversion_valid(self):
        from_currency = "USD"
        to_currency = "EUR"
        amount = 50.0
        response = currency_conversion(from_currency, to_currency, amount)
        self.assertTrue(response["success"])

    def test_currency_conversion_invalid(self):
        from_currency = "USD"
        to_currency = "XXX"
        amount = 50.0
        response = currency_conversion(from_currency, to_currency, amount)
        self.assertFalse(response["success"])


if __name__ == "__main__":
    unittest.main()
