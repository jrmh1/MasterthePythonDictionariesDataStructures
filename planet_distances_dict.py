planet_distances_dict = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.3,
    'Saturn': 1427.0,
    'Uranus': 2871.0,
    'Neptune': 4497.1
}

print("Entire dictionary:", planet_distances_dict)

third_planet_distance = list(planet_distances_dict.items())[2]
print("Distance of the 3rd planet:", third_planet_distance)

planet_distances_dict['Jupiter'] = 800.0

del planet_distances_dict['Uranus']

last_planet_distance = list(planet_distances_dict.items())[-1]
print("Last key-value pair:", last_planet_distance)
