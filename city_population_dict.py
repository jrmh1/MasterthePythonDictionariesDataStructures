
city_population = {
    'Quezon City': 2936116,
    'Manila': 1854975,
    'Davao City': 1711107,
    'Cebu City': 964169,
    'Zamboanga City': 977234,
    'Antipolo': 887399,
    'Pasig': 803159,
    'Taguig': 886722,
    'Cagayan de Oro': 728402,
    'Dasmariñas': 703141
}


print("Entire dictionary:", city_population)


sixth_key = list(city_population.keys())[5]
print(f"Population of the 6th city ({sixth_key}):", city_population[sixth_key])


third_key = list(city_population.keys())[2]
city_population[third_key] = 1750000
print(f"Updated dictionary after modifying {third_key}'s population:", city_population)


ninth_key = list(city_population.keys())[8]
del city_population[ninth_key]
print(f"Dictionary after deleting {ninth_key}:", city_population)


last_key = list(city_population.keys())[-1]
print(f"Last key-value pair: {last_key}: {city_population[last_key]}")
