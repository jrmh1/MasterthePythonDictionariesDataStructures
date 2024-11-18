plant_types_dict = {
    'Rose': 'Shrub',
    'Oak': 'Tree',
    'Lavender': 'Herb',
    'Cactus': 'Succulent',
    'Tulip': 'Flower',
    'Bamboo': 'Grass',
    'Fern': 'Fern',
    'Sunflower': 'Flower'
}

print("Entire dictionary:", plant_types_dict)

fifth_plant_type = list(plant_types_dict.items())[4]
print("Type of the 5th plant:", fifth_plant_type)

plant_types_dict['Oak'] = 'Deciduous Tree'

del plant_types_dict['Bamboo']

last_plant_type = list(plant_types_dict.items())[-1]
print("Last key-value pair:", last_plant_type)
