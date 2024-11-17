
animal_sounds = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Cow': 'Moo',
    'Sheep': 'Baa',
    'Duck': 'Quack',
    'Rooster': 'Crow',
    'Horse': 'Neigh',
    'Snake': 'Hiss'
}


print("Entire dictionary:", animal_sounds)


fourth_key = list(animal_sounds.keys())[3]
print(f"Sound of the 4th animal ({fourth_key}):", animal_sounds[fourth_key])


seventh_key = list(animal_sounds.keys())[6]
animal_sounds[seventh_key] = 'Whinny'
print(f"Updated dictionary after modifying {seventh_key}'s sound:", animal_sounds)


fifth_key = list(animal_sounds.keys())[4]
del animal_sounds[fifth_key]
print(f"Dictionary after deleting {fifth_key}:", animal_sounds)


last_key = list(animal_sounds.keys())[-1]
print(f"Last key-value pair: {last_key}: {animal_sounds[last_key]}")
