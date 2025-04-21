# In this book library app we make use of basic Python data structures to build a small library
# The library app will later be expanded through implementing more data structures and algorithms within this project. 

book1 = {
  "title": "1984", # string, not int
  "author": "George Orwell",
  "year": 1949,
  "genres": ["dystopian", "political fiction"],
  "available": True
}

book2 = {
  "title": "Brave New World",
  "author": "Aldous Huxley",
  "year": 1932,
  "genres": ["dystopian", "political fiction"],
  "available": False
}

book3 = {
  "title": "We",
  "author": "Yevgeny Zamyatin",
  "year": 1924,
  "genres": ["dystopian", "political fiction"],
  "available": True
}

books = [book1, book2]

books.append(book3)

print("Original Library:")
for book in books:
    print(book)

available_books = [b for b in books if b['available']] # list comprehension
print(f"\nAvailable books: {available_books}")

# Let's add a book that is tuple instead of dictionary and see how we can manipulate a database with data of different data structures
print("\n...Adding new book: ")
book4 = ("Fahrenheit 451", "Ray Bradbury", 1953, {"dystopia", "censorship"})
books.append(book4)

# Now the books list is of mixed types. We'll use ifs to display them accordingly
print("\nBook Titles:")
for book in books:
    if isinstance(book, dict):
        print(book["title"])
    elif isinstance(book, tuple):
        print(book[0])  # title is at index 0 

# Find common genres between two books
common_genres = list(set(books[0]["genres"]) & set(books[1]["genres"])) # Here we have a case of converting lists to sets and using &, a set operator
print(f"Common between {books[0]['title']} and {books[1]['title']}: {common_genres}")

# Since one of the books is tuple, we need to convert it to dict before exporting the books list
def normalise_books(books):
    normalised = []
    for book in books:
        if isinstance(book, tuple):
            # Convert tuple to dict -- assuming it matches structure
            title, author, year, genres = book # Unpacking
            normalised.append({
                "title": title,
                "author": author,
                "year": year,
                "genres": list(genres) if isinstance(genres, set) else genres
                
            })
        else:
            # Ensure genres are list
            book_copy = book.copy()
            book_copy["genres"] = list(book_copy["genres"]) if isinstance(book_copy["genres"], set) else book_copy["genres"]
            book_copy["available"] = book_copy.get("available", True)
            normalised.append(book_copy)
    return normalised

# If a tuple has more or fewer elements than expected, Python will raise a ValueError. So the above code only works when the tuple's structure matches

# Exporting to JSON
import json

def export_books_to_json(book_list, filename="books.json"):
    json_ready_books = normalise_books(book_list)
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(json_ready_books, f, ensure_ascii=False, indent=2)

export_books_to_json(books)
print("\nExported to books.json")
