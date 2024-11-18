artist_songs_dict = {
    'Taylor Swift': 'Anti-Hero',
    'Ed Sheeran': 'Shape of You',
    'Adele': 'Easy on Me',
    'Drake': 'God\'s Plan',
    'Billie Eilish': 'Bad Guy',
    'The Weeknd': 'Blinding Lights',
    'Dua Lipa': 'Levitating',
    'Bruno Mars': 'Uptown Funk'
}

print("Entire dictionary:", artist_songs_dict)

third_artist_song = list(artist_songs_dict.items())[2]
print("Top song of the 3rd artist:", third_artist_song)

artist_songs_dict['The Weeknd'] = 'Starboy'

del artist_songs_dict['Dua Lipa']

last_artist_song = list(artist_songs_dict.items())[-1]
print("Last key-value pair:", last_artist_song)
