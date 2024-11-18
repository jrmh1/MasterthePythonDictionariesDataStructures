phone_models_dict = {
    'iPhone 15': 'Apple',
    'Galaxy S24': 'Samsung',
    'Pixel 8': 'Google',
    'OnePlus 11': 'OnePlus',
    'Xperia 1 IV': 'Sony',
    'Moto Edge 40': 'Motorola',
    'Nokia X30': 'Nokia',
    'Huawei P60 Pro': 'Huawei',
    'LG Velvet': 'LG',
    'Google Pixel Fold': 'Google'
}

print("Entire dictionary:", phone_models_dict)

second_phone_manufacturer = list(phone_models_dict.items())[1]
print("Manufacturer of the 2nd phone model:", second_phone_manufacturer)

phone_models_dict['Huawei P60 Pro'] = 'Huawei Technologies'

del phone_models_dict['Moto Edge 40']

last_phone_manufacturer = list(phone_models_dict.items())[-1]
print("Last key-value pair:", last_phone_manufacturer)
