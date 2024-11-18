technology_inventors_dict = {
    'Telephone': 'Alexander Graham Bell',
    'Lightbulb': 'Thomas Edison',
    'Airplane': 'Wright Brothers',
    'Internet': 'Tim Berners-Lee',
    'Computer': 'Charles Babbage',
    'Television': 'John Logie Baird'
}

print("Entire dictionary:", technology_inventors_dict)

fourth_technology_inventor = list(technology_inventors_dict.items())[3]
print("Inventor of the 4th technology:", fourth_technology_inventor)

technology_inventors_dict['Lightbulb'] = 'Nikola Tesla'

del technology_inventors_dict['Television']

last_technology_inventor = list(technology_inventors_dict.items())[-1]
print("Last key-value pair:", last_technology_inventor)
