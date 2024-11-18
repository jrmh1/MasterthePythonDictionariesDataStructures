sports_players_dict = {
    'Soccer': 'Lionel Messi',
    'Basketball': 'LeBron James',
    'Tennis': 'Roger Federer',
    'Baseball': 'Babe Ruth',
    'Cricket': 'Sachin Tendulkar',
    'Boxing': 'Muhammad Ali',
    'Golf': 'Tiger Woods',
    'Rugby': 'Jonah Lomu',
    'Swimming': 'Michael Phelps',
    'American Football': 'Tom Brady'
}


print("Entire dictionary:", sports_players_dict)


fourth_sport = list(sports_players_dict.items())[3]
print("Player of the 4th sport:", fourth_sport)


sports_players_dict['Boxing'] = 'Mike Tyson'

del sports_players_dict['American Football']


last_sport = list(sports_players_dict.items())[-1]
print("Last key-value pair:", last_sport)

