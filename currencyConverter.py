from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

amount = 100  # Amount to convert
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f'{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}')
