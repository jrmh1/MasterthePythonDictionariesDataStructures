coffee_types_dict = {
    'Cold Brew': 'Coffee brewed with cold water over an extended period, resulting in a smooth, less acidic flavor.',
    'Affogato': 'A dessert coffee made by pouring a shot of hot espresso over a scoop of vanilla ice cream.',
    'Latte': 'A coffee drink made with espresso and steamed milk, typically topped with a small amount of foamed milk.',
    'Cortado': 'An espresso cut with a small amount of warm milk to reduce its acidity.',
    'Macchiato': 'An espresso coffee with a small amount of steamed milk, usually just a dollop of foam.',
    'Espresso': 'A strong, concentrated coffee brewed by forcing hot water through finely ground coffee beans.',
    'Americano': 'A diluted espresso, made by adding hot water to the espresso shot.',
    'Flat White': 'Similar to a latte, but with a higher ratio of coffee to milk and a velvety texture.',
    'Cappuccino': 'A coffee drink made with equal parts espresso, steamed milk, and foamed milk.',
    'Mocha': 'A coffee drink made with espresso, steamed milk, and chocolate syrup, often topped with whipped cream.'
}

print("Entire dictionary:", coffee_types_dict)

fourth_coffee_description = list(coffee_types_dict.items())[3]
print("Description of the 4th type of coffee:", fourth_coffee_description)

coffee_types_dict['Cortado'] = 'An espresso cut with a small amount of steamed milk, resulting in a balanced, strong flavor.'

del coffee_types_dict['Mocha']

last_coffee_description = list(coffee_types_dict.items())[-1]
print("Last key-value pair:", last_coffee_description)
