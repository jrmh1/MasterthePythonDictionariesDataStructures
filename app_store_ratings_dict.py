
app_store_ratings_dict = {
    'Instagram': 4.7,
    'TikTok': 4.5,
    'WhatsApp': 4.8,
    'Facebook': 4.3,
    'Snapchat': 4.4,
    'YouTube': 4.6,
    'Twitter': 4.2,
    'LinkedIn': 4.0,
    'Spotify': 4.3,
    'Pinterest': 4.6
}


print("Entire dictionary:", app_store_ratings_dict)


sixth_app_rating = list(app_store_ratings_dict.items())[5]
print("Rating of the 6th app:", sixth_app_rating)


app_store_ratings_dict['LinkedIn'] = 4.2


del app_store_ratings_dict['Spotify']


last_app_rating = list(app_store_ratings_dict.items())[-1]
print("Last key-value pair:", last_app_rating)
