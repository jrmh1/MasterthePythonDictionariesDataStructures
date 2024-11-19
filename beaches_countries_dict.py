beaches_countries_dict = {
    'Bondi Beach': 'Australia',
    'Waikiki Beach': 'USA',
    'Copacabana Beach': 'Brazil',
    'Maya Bay': 'Thailand',
    'Anse Source d\'Argent': 'Seychelles',
    'White Beach': 'Philippines',
    'Playa del Carmen': 'Mexico',
    'Kailua Beach': 'USA'
}

print("Entire dictionary:", beaches_countries_dict)

third_beach_country = list(beaches_countries_dict.items())[2]
print("Country of the 3rd beach:", third_beach_country)

beaches_countries_dict['White Beach'] = 'Philippines'

del beaches_countries_dict['Anse Source d\'Argent']

last_beach_country = list(beaches_countries_dict.items())[-1]
print("Last key-value pair:", last_beach_country)
