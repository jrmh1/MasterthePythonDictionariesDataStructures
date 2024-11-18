music_albums_dict = {
    '1989': 2014,
    'Future Nostalgia': 2020,
    'Folklore': 2020,
    'SOUR': 2021,
    'When We All Fall Asleep, Where Do We Go?': 2019,
    'After Hours': 2020,
    'Planet Her': 2021,
    'Midnights': 2022,
    'Montero': 2021,
    'Harry’s House': 2022
}
 
print("Entire dictionary:", music_albums_dict)

third_album_year = list(music_albums_dict.items())[2]
print("Release year of the 3rd album:", third_album_year)

music_albums_dict['Planet Her'] = 2020

del music_albums_dict['When We All Fall Asleep, Where Do We Go?']

last_album_year = list(music_albums_dict.items())[-1]
print("Last key-value pair:", last_album_year)
