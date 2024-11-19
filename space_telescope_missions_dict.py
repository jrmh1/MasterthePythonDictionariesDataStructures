space_telescope_missions_dict = {
    'Voyager 1': 'Exploration of the outer planets and interstellar space',
    'WISE': 'Wide-field Infrared Survey Explorer mission',
    'TESS': 'Transiting Exoplanet Survey Satellite mission',
    'Gaia': 'Galactic mapping and star cataloging mission',
    'SOHO': 'Solar and Heliospheric Observatory mission'
}

print("Entire dictionary:", space_telescope_missions_dict)

second_telescope_mission = list(space_telescope_missions_dict.items())[1]
print("Mission of the 2nd telescope:", second_telescope_mission)

space_telescope_missions_dict['SOHO'] = 'Updated solar observation mission'

del space_telescope_missions_dict['TESS']

last_telescope_mission = list(space_telescope_missions_dict.items())[-1]
print("Last key-value pair:", last_telescope_mission)
