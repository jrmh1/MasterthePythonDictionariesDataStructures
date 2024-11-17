
software_companies = {
    'Microsoft': 'Redmond, Washington, USA',
    'Apple': 'Cupertino, California, USA',
    'Google': 'Mountain View, California, USA',
    'Amazon': 'Seattle, Washington, USA',
    'Facebook': 'Menlo Park, California, USA',
    'IBM': 'Armonk, New York, USA',
    'Oracle': 'Austin, Texas, USA',
    'Salesforce': 'San Francisco, California, USA',
    'Adobe': 'San Jose, California, USA',
    'Intel': 'Santa Clara, California, USA'
}


print("Entire dictionary:", software_companies)


third_key = list(software_companies.keys())[2]
print(f"Headquarters of the 3rd company ({third_key}):", software_companies[third_key])


eighth_key = list(software_companies.keys())[7]
software_companies[eighth_key] = 'Updated Location'
print(f"Updated dictionary after modifying {eighth_key}'s headquarters:", software_companies)

ninth_key = list(software_companies.keys())[8]
del software_companies[ninth_key]
print(f"Dictionary after deleting {ninth_key}:", software_companies)


last_key = list(software_companies.keys())[-1]
print(f"Last key-value pair: {last_key}: {software_companies[last_key]}")
