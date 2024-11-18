
river_lengths_dict = {
    'Nile': 6650,
    'Amazon': 6400,
    'Yangtze': 6300,
    'Mississippi': 3730,
    'Yenisei': 5539,
    'Yellow River': 5464
}


print("Entire dictionary:", river_lengths_dict)


second_river_length = list(river_lengths_dict.items())[1]
print("Length of the 2nd river:", second_river_length)


river_lengths_dict['Yenisei'] = 5600


del river_lengths_dict['Mississippi']


last_river_length = list(river_lengths_dict.items())[-1]
print("Last key-value pair:", last_river_length)
