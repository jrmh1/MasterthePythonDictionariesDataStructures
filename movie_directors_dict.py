movie_directors = {
    'The Lion King': 'Roger Allers & Rob Minkoff',
    'Toy Story': 'John Lasseter',
    'Spirited Away': 'Hayao Miyazaki',
    'Frozen': 'Chris Buck & Jennifer Lee',
    'Finding Nemo': 'Andrew Stanton',
    'Shrek': 'Andrew Adamson & Vicky Jenson',
    'Coco': 'Lee Unkrich & Adrian Molina',
    'The Incredibles': 'Brad Bird',
    'How to Train Your Dragon': 'Dean DeBlois',
    'Zootopia': 'Byron Howard & Rich Moore'
}

print("Entire dictionary:", movie_directors)

fifth_key = list(movie_directors.keys())[4]
print(f"Director of the 5th movie ({fifth_key}):", movie_directors[fifth_key])

ninth_key = list(movie_directors.keys())[8]
movie_directors[ninth_key] = 'Updated Director'
print(f"Updated dictionary after modifying {ninth_key}'s director:", movie_directors)

seventh_key = list(movie_directors.keys())[6]
del movie_directors[seventh_key]
print(f"Dictionary after deleting {seventh_key}:", movie_directors)

last_key = list(movie_directors.keys())[-1]
print(f"Last key-value pair: {last_key}: {movie_directors[last_key]}")
