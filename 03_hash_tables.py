"""
HASH TABLES
Linking keys with values:

user_ages = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}
print(user_ages["Bob"])  # 25

Python dictionaries are, in fact, highly optimised hash tables with in-built hash functions for different types which dynamically resize for efficiency.

The custom implementation of hash tables show what actually happens under the hood.

But when working with dictionaries in Python/JS, you generally don't have to worry about hash table implementation details like size, buckets, or collision resolution.
"""

class BookHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)] # Array of empty lists. Each list is a bucket that can store multiple key-value pairs.

    def _hash(self, key):
        # converts a key into an integer index that tells us which bucket to use
        return hash(key) % self.size

    def insert(self, title, author, year, genres):
        index = self._hash(title)
        bucket = self.table[index]

        for entry in bucket:
            if entry[0] == title:
                entry[1] = {
                    "author": author,
                    "year": year,
                    "genres": genres
                }
                return
        
        bucket.append((title, {
            "author": author,
            "year": year,
            "genres": genres
        }))

    def get(self, title):
        index = self._hash(title)
        bucket = self.table[index]

        for entry in bucket:
            if entry[0] == title:
                return entry[1]
        return None

    def delete(self, title):
        index = self._hash(title)
        bucket = self.table[index]

        for i, entry in enumerate(bucket):
            if entry[0] == title:
                del bucket[i]
                return True
        return False

    def list_books(self):
        all_books = []
        for bucket in self.table:
            for title, info in bucket:
                all_books.append((title, info))
        return all_books

library = BookHashTable()

# Добавяне
library.insert("1984", "George Orwell", 1949, ["dystopian", "political fiction"])
library.insert("Brave New World", "Aldous Huxley", 1932, ["dystopian", "science fiction"])
library.insert("Dune", "Frank Herbert", 1965, ["science fiction", "epic"])

# Извличане
book = library.get("1984")
print("Fetched:", book)

# Изтриване
library.delete("Brave New World")

# Изброяване на книги
for title, info in library.list_books():
    print(f"{title} by {info['author']} ({info['year']}) → Genres: {', '.join(info['genres'])}")

