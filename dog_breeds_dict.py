dog_breeds_dict = {
    'Beagle': 'Medium',
    'Chihuahua': 'Small',
    'Golden Retriever': 'Large',
    'German Shepherd': 'Large',
    'Poodle': 'Medium',
    'Bulldog': 'Medium',
    'Rottweiler': 'Large',
    'Dachshund': 'Small',
    'Boxer': 'Medium',
    'Labrador Retriever': 'Large'
}

print("Entire dictionary:", dog_breeds_dict)

fifth_breed_size = list(dog_breeds_dict.items())[4]
print("Size of the 5th breed:", fifth_breed_size)

dog_breeds_dict['Dachshund'] = 'Medium'

del dog_breeds_dict['Bulldog']

last_breed_size = list(dog_breeds_dict.items())[-1]
print("Last key-value pair:", last_breed_size)
