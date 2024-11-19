space_telescope_missions = {
    'Hubble': 'Exploration of deep space',
    'Chandra': 'X-ray observations of black holes',
    'James Webb': 'Studying the early universe',
    'Spitzer': 'Infrared observations of galaxies',
    'Kepler': 'Searching for exoplanets'
}

print("Space Telescope Missions Dictionary:", space_telescope_missions)

print("Mission of the third telescope (James Webb):", space_telescope_missions['James Webb'])

space_telescope_missions['Hubble'] = 'Observing distant galaxies and supernovae'
print("Updated mission of the first telescope (Hubble):", space_telescope_missions['Hubble'])

del space_telescope_missions['Spitzer']
print("Dictionary after deleting the 4th telescope:", space_telescope_missions)

last_key = list(space_telescope_missions.keys())[-1]
print("Last key-value pair:", last_key, ":", space_telescope_missions[last_key])
