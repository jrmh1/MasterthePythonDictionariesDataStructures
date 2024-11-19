food_recipes_dict = {
    'Pizza': 'Dough, tomato sauce, cheese, toppings of choice, baked in oven.',
    'Pasta': 'Boil pasta, add tomato sauce, garlic, olive oil, and cheese.',
    'Burger': 'Grilled patty, lettuce, tomato, cheese, ketchup, on a bun.',
    'Sushi': 'Rice, seaweed, fish or vegetables, rolled and sliced.',
    'Salad': 'Mixed greens, tomatoes, cucumbers, dressing of choice.',
    'Tacos': 'Taco shells, seasoned meat, lettuce, cheese, salsa.',
    'Steak': 'Seasoned beef steak, grilled or pan-fried to desired doneness.',
    'Pancakes': 'Flour, eggs, milk, sugar, baking powder, cooked on a griddle.'
}

print("Entire dictionary:", food_recipes_dict)

fifth_food_recipe = list(food_recipes_dict.items())[4]
print("Recipe of the 5th food:", fifth_food_recipe)

food_recipes_dict['Burger'] = 'Grilled patty, lettuce, tomato, cheese, pickles, ketchup, on a bun.'

del food_recipes_dict['Steak']

last_food_recipe = list(food_recipes_dict.items())[-1]
print("Last key-value pair:", last_food_recipe)
