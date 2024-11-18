
flower_meanings_dict = {
    'Rose': 'Love',
    'Lily': 'Purity',
    'Tulip': 'Perfect Love',
    'Daffodil': 'Rebirth',
    'Sunflower': 'Adoration',
    'Orchid': 'Beauty',
    'Violet': 'Modesty',
    'Daisy': 'Innocence'
}


print("Entire dictionary:", flower_meanings_dict)


fifth_flower_meaning = list(flower_meanings_dict.items())[4]
print("Meaning of the 5th flower:", fifth_flower_meaning)


flower_meanings_dict['Violet'] = 'Faithfulness'


del flower_meanings_dict['Orchid']


last_flower_meaning = list(flower_meanings_dict.items())[-1]
print("Last key-value pair:", last_flower_meaning)
