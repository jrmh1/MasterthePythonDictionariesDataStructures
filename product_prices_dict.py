
product_prices_dict = {
    'Laptop': 899.99,
    'Smartphone': 499.99,
    'Headphones': 89.99,
    'Monitor': 199.99,
    'Keyboard': 49.99,
    'Mouse': 29.99,
    'Speaker': 129.99,
    'Charger': 19.99,
    'Tablet': 349.99,
    'Smartwatch': 229.99
}


print("Entire dictionary:", product_prices_dict)


fourth_product_price = list(product_prices_dict.items())[3]
print("Price of the 4th product:", fourth_product_price)


product_prices_dict['Tablet'] = 329.99


del product_prices_dict['Mouse']


last_product_price = list(product_prices_dict.items())[-1]
print("Last key-value pair:", last_product_price)
