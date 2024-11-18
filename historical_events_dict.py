historical_events_dict = {
    'American Revolution': 1775,
    'French Revolution': 1789,
    'World War I': 1914,
    'World War II': 1939,
    'Apollo 11 Moon Landing': 1969,
    'Fall of the Berlin Wall': 1989,
    'End of Apartheid in South Africa': 1994,
    'September 11 Attacks': 2001
}

print("Entire dictionary:", historical_events_dict)

second_event_year = list(historical_events_dict.items())[1]
print("Year of the 2nd event:", second_event_year)

historical_events_dict['End of Apartheid in South Africa'] = 1995

del historical_events_dict['Apollo 11 Moon Landing']

last_event_year = list(historical_events_dict.items())[-1]
print("Last key-value pair:", last_event_year)
