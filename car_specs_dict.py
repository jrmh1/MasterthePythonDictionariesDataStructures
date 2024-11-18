car_specs_dict = {
    'Tesla Model S': 'Electric, 1020 hp, 0-60 mph in 2.1s',
    'BMW M3': '3.0L I6, 473 hp, 0-60 mph in 3.8s',
    'Ford Mustang GT': '5.0L V8, 450 hp, 0-60 mph in 4.2s',
    'Chevrolet Corvette': '6.2L V8, 495 hp, 0-60 mph in 2.9s',
    'Audi R8': '5.2L V10, 562 hp, 0-60 mph in 3.3s',
    'Porsche 911 Turbo': '3.8L I6, 572 hp, 0-60 mph in 2.7s',
    'Mercedes-Benz AMG GT': '4.0L V8, 523 hp, 0-60 mph in 3.6s',
    'Jaguar F-Type': '5.0L V8, 575 hp, 0-60 mph in 3.5s',
    'Lamborghini Aventador': '6.5L V12, 730 hp, 0-60 mph in 2.9s',
    'Ferrari 488 GTB': '3.9L V8, 661 hp, 0-60 mph in 3.0s'
}

print("Entire dictionary:", car_specs_dict)

fourth_car_specs = list(car_specs_dict.items())[3]
print("Specifications of the 4th car model:", fourth_car_specs)

car_specs_dict['Lamborghini Aventador'] = '6.5L V12, 770 hp, 0-60 mph in 2.7s'

del car_specs_dict['Audi R8']

last_car_specs = list(car_specs_dict.items())[-1]
print("Last key-value pair:", last_car_specs)
