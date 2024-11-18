
movie_genres_dict = {
    'Action': 'Mad Max: Fury Road',
    'Comedy': 'Superbad',
    'Drama': 'The Shawshank Redemption',
    'Horror': 'The Conjuring',
    'Sci-Fi': 'Interstellar',
    'Romance': 'The Notebook',
    'Thriller': 'Gone Girl',
    'Animation': 'Toy Story'
}


print("Entire dictionary:", movie_genres_dict)


third_genre_movie = list(movie_genres_dict.items())[2]
print("Example movie of the 3rd genre:", third_genre_movie)

movie_genres_dict['Sci-Fi'] = 'Inception'

del movie_genres_dict['Thriller']

last_genre_movie = list(movie_genres_dict.items())[-1]
print("Last key-value pair:", last_genre_movie)
