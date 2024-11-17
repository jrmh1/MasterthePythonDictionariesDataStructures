
country_capital = {
    'Philippines': 'Manila',
    'USA': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Japan': 'Tokyo',
    'India': 'New Delhi',
    'Australia': 'Canberra',
    'Brazil': 'Brasilia',
    'South Africa': 'Pretoria',
    'Italy': 'Rome',
    'Spain': 'Madrid'
}


print("Entire dictionary:", country_capital)


fifth_key = list(country_capital.keys())[4]
print(f"Capital of the 5th country ({fifth_key}):", country_capital[fifth_key])


eighth_key = list(country_capital.keys())[7]
country_capital[eighth_key] = 'Rio de Janeiro'
print(f"Updated dictionary after modifying {eighth_key}'s capital:", country_capital)


eleventh_key = list(country_capital.keys())[10]
del country_capital[eleventh_key]
print(f"Dictionary after deleting {eleventh_key}:", country_capital)


last_key = list(country_capital.keys())[-1]
print(f"Last key-value pair: {last_key}: {country_capital[last_key]}")
