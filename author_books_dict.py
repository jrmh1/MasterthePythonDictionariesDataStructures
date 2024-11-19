author_books_dict = {
    'Leo Tolstoy': 'War and Peace',
    'Gabriel Garcia Marquez': 'One Hundred Years of Solitude',
    'Homer': 'The Iliad',
    'Mary Shelley': 'Frankenstein',
    'Ernest Hemingway': 'The Old Man and the Sea',
    'Virginia Woolf': 'Mrs. Dalloway',
    'Agatha Christie': 'Murder on the Orient Express',
    'James Joyce': 'Ulysses'
}

print("Entire dictionary:", author_books_dict)

third_author_book = list(author_books_dict.items())[2]
print("Book of the 3rd author:", third_author_book)

author_books_dict['Virginia Woolf'] = 'To the Lighthouse'

del author_books_dict['Mary Shelley']

last_author_book = list(author_books_dict.items())[-1]
print("Last key-value pair:", last_author_book)
