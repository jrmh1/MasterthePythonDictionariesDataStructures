city_landmarks_dict = {
    'Paris': 'Eiffel Tower',
    'New York': 'Statue of Liberty',
    'London': 'Big Ben',
    'Rome': 'Colosseum',
    'Sydney': 'Sydney Opera House',
    'Dubai': 'Burj Khalifa',
    'Moscow': 'Red Square',
    'Tokyo': 'Tokyo Tower'
}

print("Entire dictionary:", city_landmarks_dict)

sixth_city_landmark = list(city_landmarks_dict.items())[5]
print("Landmark of the 6th city:", sixth_city_landmark)

city_landmarks_dict['New York'] = 'Empire State Building'

del city_landmarks_dict['Moscow']

last_city_landmark = list(city_landmarks_dict.items())[-1]
print("Last key-value pair:", last_city_landmark)
