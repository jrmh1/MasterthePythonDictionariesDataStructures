technology_innovators_dict = {
    'World Wide Web': 'Tim Berners-Lee',
    'Television': 'John Logie Baird',
    'Computers': 'Charles Babbage',
    'Smartphones': 'Frank Canova',
    'Internet': 'Vinton Cerf ',
    'Electric Cars': 'Andreas Flocken',
    'Social Media': 'Andrew Weinreich',
    'Artificial Intelligence': 'John McCarthy'
}

print("Entire dictionary:", technology_innovators_dict)

fourth_technology_innovator = list(technology_innovators_dict.items())[3]
print("Innovator of the 4th technology:", fourth_technology_innovator)

technology_innovators_dict['Television'] = 'Philo Farnsworth'

del technology_innovators_dict['Electric Cars']

last_technology_innovator = list(technology_innovators_dict.items())[-1]
print("Last key-value pair:", last_technology_innovator)
