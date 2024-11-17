
fruit_colors = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Grapes': 'Purple',
    'Orange': 'Orange',
    'Watermelon': 'Green',
    'Blueberry': 'Blue',
    'Pineapple': 'Brown',
    'Strawberry': 'Red'
}


print("Entire dictionary:", fruit_colors)


sixth_key = list(fruit_colors.keys())[5]
print(f"Color of the 6th fruit ({sixth_key}):", fruit_colors[sixth_key])


fourth_key = list(fruit_colors.keys())[3]
fruit_colors[fourth_key] = 'Dark Orange'
print(f"Updated dictionary after modifying {fourth_key}'s color:", fruit_colors)


seventh_key = list(fruit_colors.keys())[6]
del fruit_colors[seventh_key]
print(f"Dictionary after deleting {seventh_key}:", fruit_colors)


last_key = list(fruit_colors.keys())[-1]
print(f"Last key-value pair: {last_key}: {fruit_colors[last_key]}")
