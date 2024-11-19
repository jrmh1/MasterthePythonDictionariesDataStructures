dinosaur_fossils_dict = {
    'Velociraptor': 'Asia',
    'Allosaurus': 'North America',
    'Triceratops': 'North America',
    'Brachiosaurus': 'North America',
    'Tyrannosaurus rex': 'North America',
    'Stegosaurus': 'North America',
    'Spinosaurus': 'Africa'
}

print("Entire dictionary:", dinosaur_fossils_dict)

fourth_dinosaur_fossils = list(dinosaur_fossils_dict.items())[3]
print("Location of the 4th dinosaur's fossils:", fourth_dinosaur_fossils)

dinosaur_fossils_dict['Triceratops'] = 'Montana, USA'

del dinosaur_fossils_dict['Stegosaurus']

last_dinosaur_fossils = list(dinosaur_fossils_dict.items())[-1]
print("Last key-value pair:", last_dinosaur_fossils)
