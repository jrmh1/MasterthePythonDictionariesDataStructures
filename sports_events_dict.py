sports_events_dict = {
    'NBA Finals': 2023,
    'Wimbledon': 2024,
    'FIFA World Cup': 2022,
    'Tour de France': 2023,
    'Super Bowl': 2023,
    'UEFA Champions League': 2024,
    'Olympic Games': 2024
}

print("Entire dictionary:", sports_events_dict)

third_event_year = list(sports_events_dict.items())[2]
print("Year of the 3rd sports event:", third_event_year)

sports_events_dict['Wimbledon'] = 2025

del sports_events_dict['FIFA World Cup']

last_event_year = list(sports_events_dict.items())[-1]
print("Last key-value pair:", last_event_year)
