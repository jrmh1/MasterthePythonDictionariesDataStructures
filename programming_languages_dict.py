programming_languages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C': 'Dennis Ritchie',
    'C++': 'Bjarne Stroustrup',
    'JavaScript': 'Brendan Eich',
    'Ruby': 'Yukihiro Matsumoto',
    'Go': 'Robert Griesemer, Rob Pike, and Ken Thompson'
}


print("Entire dictionary:", programming_languages)


fourth_key = list(programming_languages.keys())[3]
print(f"Developer of the 4th programming language ({fourth_key}):", programming_languages[fourth_key])


sixth_key = list(programming_languages.keys())[5]
programming_languages[sixth_key] = 'Matz (Yukihiro Matsumoto)'
print(f"Updated dictionary after modifying {sixth_key}'s developer:", programming_languages)


second_key = list(programming_languages.keys())[1]
del programming_languages[second_key]
print(f"Dictionary after deleting {second_key}:", programming_languages)


last_key = list(programming_languages.keys())[-1]
print(f"Last key-value pair: {last_key}: {programming_languages[last_key]}")
