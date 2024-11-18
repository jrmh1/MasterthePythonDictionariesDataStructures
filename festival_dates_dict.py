festival_dates_dict = {
    'Diwali': 'November 12, 2023',
    'Christmas': 'December 25, 2023',
    'Eid al-Fitr': 'April 21, 2024',
    'Holi': 'March 25, 2024',
    'Thanksgiving': 'November 28, 2024',
    'Lunar New Year': 'February 10, 2024',
    'Halloween': 'October 31, 2024',
    'Oktoberfest': 'September 21, 2024',
    'Valentine\'s Day': 'February 14, 2024',
    'New Year\'s Eve': 'December 31, 2024'
}

print("Entire dictionary:", festival_dates_dict)

third_festival_date = list(festival_dates_dict.items())[2]
print("Date of the 3rd festival:", third_festival_date)


festival_dates_dict['Halloween'] = 'October 31, 2025'


del festival_dates_dict['Thanksgiving']


last_festival_date = list(festival_dates_dict.items())[-1]
print("Last key-value pair:", last_festival_date)
