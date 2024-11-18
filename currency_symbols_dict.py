currency_symbols_dict = {
    'PHP': '₱',
    'USD': '$',
    'EUR': '€',
    'JPY': '¥',
    'AUD': 'A$',
    'CAD': 'C$',
    'INR': '₹',
    'CNY': '¥',
    'MXN': '$',
    'BRL': 'R$'
}

print("Entire dictionary:", currency_symbols_dict)

fifth_currency_symbol = list(currency_symbols_dict.items())[4]
print("Symbol of the 5th currency:", fifth_currency_symbol)

currency_symbols_dict['MXN'] = 'Mex$'

del currency_symbols_dict['JPY']

last_currency_symbol = list(currency_symbols_dict.items())[-1]
print("Last key-value pair:", last_currency_symbol)
