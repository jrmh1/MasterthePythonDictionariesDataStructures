festival_locations_dict = {
    'Sinulog Festival': 'Cebu City',
    'Ati-Atihan Festival': 'Kalibo, Aklan',
    'Pahiyas Festival': 'Lucban, Quezon',
    'Kadayawan Festival': 'Davao City',
    'Panagbenga Festival': 'Baguio City',
    'MassKara Festival': 'Bacolod City',
    'Dinagyang Festival': 'Iloilo City',
    'Moriones Festival': 'Marinduque'
}

print("Entire dictionary:", festival_locations_dict)

fourth_festival_location = list(festival_locations_dict.items())[3]
print("Location of the 4th festival:", fourth_festival_location)

festival_locations_dict['MassKara Festival'] = 'Bacolod, Negros Occidental'

del festival_locations_dict['Ati-Atihan Festival']

last_festival_location = list(festival_locations_dict.items())[-1]
print("Last key-value pair:", last_festival_location)
