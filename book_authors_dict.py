
book_authors = {
    'To Kill a Mockingbird': 'Harper Lee',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby Dick': 'Herman Melville',
    'War and Peace': 'Leo Tolstoy',
    'The Catcher in the Rye': 'J.D. Salinger',
    'Crime and Punishment': 'Fyodor Dostoevsky',
    'The Odyssey': 'Homer',
    'Jane Eyre': 'Charlotte Bronte',
    'The Hobbit': 'J.R.R. Tolkien',
    'Ulysses': 'James Joyce'
}


print("Entire dictionary:", book_authors)


ninth_key = list(book_authors.keys())[8]
print(f"Author of the 9th book ({ninth_key}):", book_authors[ninth_key])


fifth_key = list(book_authors.keys())[4]
book_authors[fifth_key] = 'Updated Author'
print(f"Updated dictionary after modifying {fifth_key}'s author:", book_authors)


third_key = list(book_authors.keys())[2]
del book_authors[third_key]
print(f"Dictionary after deleting {third_key}:", book_authors)


last_key = list(book_authors.keys())[-1]
print(f"Last key-value pair: {last_key}: {book_authors[last_key]}")
