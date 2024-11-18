
animal_habitats_dict = {
    'Lion': 'Savanna',
    'Penguin': 'Antarctica',
    'Kangaroo': 'Australian Outback',
    'Elephant': 'Grasslands',
    'Polar Bear': 'Arctic',
    'Giraffe': 'Savanna',
    'Panda': 'Bamboo Forest',
    'Tiger': 'Tropical Rainforest'
}


print("Entire dictionary:", animal_habitats_dict)


third_animal_habitat = list(animal_habitats_dict.items())[2]
print("Habitat of the 3rd animal:", third_animal_habitat)


animal_habitats_dict['Polar Bear'] = 'Tundra'


del animal_habitats_dict['Panda']


last_animal_habitat = list(animal_habitats_dict.items())[-1]
print("Last key-value pair:", last_animal_habitat)
