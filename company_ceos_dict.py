company_ceos_dict = {
    'Apple': 'Tim Cook',
    'Microsoft': 'Satya Nadella',
    'Amazon': 'Andy Jassy',
    'Tesla': 'Elon Musk',
    'Google': 'Sundar Pichai',
    'Facebook': 'Mark Zuckerberg',
    'Netflix': 'Reed Hastings',
    'IBM': 'Arvind Krishna',
    'Twitter': 'Elon Musk',
    'Adobe': 'Shantanu Narayen'
}


print("Entire dictionary:", company_ceos_dict)


sixth_company_ceo = list(company_ceos_dict.items())[5]
print("CEO of the 6th company:", sixth_company_ceo)


company_ceos_dict['Amazon'] = 'Jeff Bezos'


del company_ceos_dict['Twitter']


last_company_ceo = list(company_ceos_dict.items())[-1]
print("Last key-value pair:", last_company_ceo)
