video_game_platforms_dict = {
    'The Legend of Zelda: Breath of the Wild': 'Nintendo Switch',
    'Super Mario Odyssey': 'Nintendo Switch',
    'Minecraft': 'Multiple Platforms',
    'Red Dead Redemption 2': 'PlayStation 4, Xbox One, PC',
    'Fortnite': 'Multiple Platforms',
    'The Last of Us Part II': 'PlayStation 4',
    'God of War': 'PlayStation 4',
    'Animal Crossing: New Horizons': 'Nintendo Switch'
}

print("Entire dictionary:", video_game_platforms_dict)

second_game_platform = list(video_game_platforms_dict.items())[1]
print("Platform of the 2nd video game:", second_game_platform)

video_game_platforms_dict['The Last of Us Part II'] = 'PlayStation 5'

del video_game_platforms_dict['Red Dead Redemption 2']

last_game_platform = list(video_game_platforms_dict.items())[-1]
print("Last key-value pair:", last_game_platform)
