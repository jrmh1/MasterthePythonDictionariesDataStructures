software_versions_dict = {
    'Windows 11': '22H2',
    'macOS Sonoma': '14.1',
    'Ubuntu': '23.10',
    'Google Chrome': '117.0.5938.92',
    'Visual Studio Code': '1.85.0',
    'Adobe Photoshop': '2024.1'
}

print("Entire dictionary:", software_versions_dict)

fourth_software_version = list(software_versions_dict.items())[3]
print("Version of the 4th software:", fourth_software_version)

software_versions_dict['macOS Sonoma'] = '14.2'

del software_versions_dict['Visual Studio Code']

last_software_version = list(software_versions_dict.items())[-1]
print("Last key-value pair:", last_software_version)
