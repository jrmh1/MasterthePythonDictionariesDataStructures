province_capitals_dict = {
    'Cebu': 'Cebu City',
    'Bohol': 'Tagbilaran City',
    'Palawan': 'Puerto Princesa',
    'Iloilo': 'Iloilo City',
    'Davao del Sur': 'Davao City',
    'Batangas': 'Batangas City',
    'Pampanga': 'San Fernando',
    'Laguna': 'Santa Cruz',
    'Cagayan': 'Tuguegarao',
    'Albay': 'Legazpi City'
}

print("Entire dictionary:", province_capitals_dict)

fourth_province_capital = list(province_capitals_dict.items())[3]
print("Capital of the 4th province:", fourth_province_capital)

province_capitals_dict['Laguna'] = 'Calamba'

del province_capitals_dict['Pampanga']

last_province_capital = list(province_capitals_dict.items())[-1]
print("Last key-value pair:", last_province_capital)
