
space_missions_dict = {
    'Apollo 11': 1969,
    'Voyager 1': 1977,
    'Curiosity Rover': 2012,
    'New Horizons': 2015,
    'Perseverance Rover': 2020
}


print("Entire dictionary:", space_missions_dict)


third_mission_year = list(space_missions_dict.items())[2]
print("Year of the 3rd mission:", third_mission_year)


space_missions_dict['Voyager 1'] = 1978


del space_missions_dict['New Horizons']


last_mission_year = list(space_missions_dict.items())[-1]
print("Last key-value pair:", last_mission_year)
