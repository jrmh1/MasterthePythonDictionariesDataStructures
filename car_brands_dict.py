
car_brands = {
    'Toyota': 'Japan',
    'Ford': 'USA',
    'BMW': 'Germany',
    'Hyundai': 'South Korea',
    'Ferrari': 'Italy',
    'Volkswagen': 'Germany',
    'Honda': 'Japan',
    'Renault': 'France',
    'Tesla': 'USA',
    'Volvo': 'Sweden'
}


print("Entire dictionary:", car_brands)


third_key = list(car_brands.keys())[2]
print(f"Country of origin of the 3rd car brand ({third_key}):", car_brands[third_key])


seventh_key = list(car_brands.keys())[6]
car_brands[seventh_key] = 'South Korea'
print(f"Updated dictionary after modifying {seventh_key}'s country of origin:", car_brands)


eighth_key = list(car_brands.keys())[7]
del car_brands[eighth_key]
print(f"Dictionary after deleting {eighth_key}:", car_brands)


last_key = list(car_brands.keys())[-1]
print(f"Last key-value pair: {last_key}: {car_brands[last_key]}")
