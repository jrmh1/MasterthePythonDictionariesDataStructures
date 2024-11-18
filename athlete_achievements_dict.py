athlete_achievements_dict = {
    'Usain Bolt': '8 Olympic Gold Medals',
    'Michael Phelps': '23 Olympic Gold Medals',
    'Serena Williams': '23 Grand Slam Singles Titles',
    'Cristiano Ronaldo': '5 Ballon d\'Or Awards',
    'LeBron James': '4 NBA Championships',
    'Roger Federer': '20 Grand Slam Singles Titles',
    'Simone Biles': '7 Olympic Medals',
    'Lionel Messi': '7 Ballon d\'Or Awards'
}

print("Entire dictionary:", athlete_achievements_dict)

fifth_athlete_achievement = list(athlete_achievements_dict.items())[4]
print("Achievement of the 5th athlete:", fifth_athlete_achievement)

athlete_achievements_dict['Serena Williams'] = '24 Grand Slam Singles Titles'

del athlete_achievements_dict['Simone Biles']

last_athlete_achievement = list(athlete_achievements_dict.items())[-1]
print("Last key-value pair:", last_athlete_achievement)
