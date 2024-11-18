
holiday_dates_dict = {
    'New Year\'s Day': 'January 1',
    'Valentine\'s Day': 'February 14',
    'Easter': 'April 9',
    'Independence Day': 'July 4',
    'Halloween': 'October 31',
    'Thanksgiving': 'November 28',
    'Christmas': 'December 25',
    'Labor Day': 'First Monday in September',
    'Memorial Day': 'Last Monday in May',
    'Veterans Day': 'November 11'
}


print("Entire dictionary:", holiday_dates_dict)


fourth_holiday_date = list(holiday_dates_dict.items())[3]
print("Date of the 4th holiday:", fourth_holiday_date)


holiday_dates_dict['Memorial Day'] = 'May 30'


del holiday_dates_dict['Valentine\'s Day']


last_holiday_date = list(holiday_dates_dict.items())[-1]
print("Last key-value pair:", last_holiday_date)
