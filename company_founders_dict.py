company_founders_dict = {
    'Apple': 'Steve Jobs',
    'Microsoft': 'Bill Gates',
    'Google': 'Larry Page & Sergey Brin',
    'Amazon': 'Jeff Bezos',
    'Tesla': 'Elon Musk',
    'Facebook': 'Mark Zuckerberg',
    'Adobe': 'John Warnock & Charles Geschke',
    'Netflix': 'Reed Hastings & Marc Randolph'
}

print("Entire dictionary:", company_founders_dict)

sixth_company_founder = list(company_founders_dict.items())[5]
print("Founder of the 6th company:", sixth_company_founder)

company_founders_dict['Microsoft'] = 'Bill Gates & Paul Allen'

del company_founders_dict['Netflix']

last_company_founder = list(company_founders_dict.items())[-1]
print("Last key-value pair:", last_company_founder)
