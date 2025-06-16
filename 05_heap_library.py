import heapq
from copy import deepcopy

# Import the tree library
from tree_library import BookTreeLibrary  # Make sure filename matches

class BookHeapLibrary:
    def __init__(self):
        self.tree_library = BookTreeLibrary()
        self.popularity_min_heap = []  # Min heap for least popular books
        self.popularity_max_heap = []  # Max heap (with negative values) for most popular books
        self.year_min_heap = []        # For finding oldest books
        self.checkout_count = {}       # Track number of checkouts per book
        self.checkout_heap = []        # Track checkout frequency
    
    def add_book(self, title, author, year, genres, popularity=0):
        # Add to the balanced tree
        book = self.tree_library.add_book(title, author, year, genres, popularity)
        
        # Add to heaps
        heapq.heappush(self.popularity_min_heap, (popularity, title))
        heapq.heappush(self.popularity_max_heap, (-popularity, title))  # Negative for max heap
        heapq.heappush(self.year_min_heap, (year, title))
        
        # Initialize checkout count
        self.checkout_count[title] = 0
        
        return book
    
    def add_books_from_list(self, books):
        """Add multiple books from a list of dictionaries"""
        for book in books:
            self.add_book(
                book["title"], 
                book["author"], 
                book["year"], 
                book.get("genres", []), 
                book.get("popularity", 0)
            )
    
    def checkout_book(self, title):
        """Record a book checkout, updating its frequency in the heap"""
        # Increment checkout count
        if title in self.checkout_count:
            self.checkout_count[title] += 1
            count = self.checkout_count[title]
            
            # Add to checkout heap (negative count for max heap behavior)
            heapq.heappush(self.checkout_heap, (-count, title))
            
            return True
        return False
    
    def get_least_popular_books(self, n=3):
        """Use min heap to find least popular books for promotion"""
        # Create a copy of the heap to avoid modifying the original
        heap_copy = deepcopy(self.popularity_min_heap)
        result = []
        
        for _ in range(min(n, len(heap_copy))):
            if heap_copy:
                popularity, title = heapq.heappop(heap_copy)
                book = self.tree_library.search_by_title(title)
                if book:
                    result.append(book)
        
        return result
    
    def get_most_popular_books(self, n=3):
        """Use max heap to find most popular books for recommendations"""
        # Create a copy of the heap to avoid modifying the original
        heap_copy = deepcopy(self.popularity_max_heap)
        result = []
        
        for _ in range(min(n, len(heap_copy))):
            if heap_copy:
                neg_popularity, title = heapq.heappop(heap_copy)
                book = self.tree_library.search_by_title(title)
                if book:
                    book["popularity"] = -neg_popularity  # Convert back to positive
                    result.append(book)
        
        return result
    
    def get_oldest_books(self, n=3):
        """Find the oldest books in the library"""
        heap_copy = deepcopy(self.year_min_heap)
        result = []
        
        for _ in range(min(n, len(heap_copy))):
            if heap_copy:
                year, title = heapq.heappop(heap_copy)
                book = self.tree_library.search_by_title(title)
                if book:
                    result.append(book)
        
        return result
    
    def get_most_checked_out_books(self, n=3):
        """Find books with highest checkout frequency"""
        # Using the checkout heap
        heap_copy = deepcopy(self.checkout_heap)
        result = []
        processed_titles = set()  # To handle duplicates
        
        while len(result) < n and heap_copy:
            neg_count, title = heapq.heappop(heap_copy)
            if title not in processed_titles:
                processed_titles.add(title)
                book = self.tree_library.search_by_title(title)
                if book:
                    book["checkout_count"] = -neg_count  # Convert back to positive
                    result.append(book)
        
        return result
    
    def update_popularity(self, title, new_popularity):
        """Update a book's popularity score"""
        # Find and update in tree
        book = self.tree_library.search_by_title(title)
        if not book:
            return False
        
        # For this demo, we'll just add a new entry to the heaps
        # In a real system, you'd want to find and remove the old entry first
        heapq.heappush(self.popularity_min_heap, (new_popularity, title))
        heapq.heappush(self.popularity_max_heap, (-new_popularity, title))
        
        return True
    
    # Search and traversal methods can use the tree library directly
    def search_by_title(self, title):
        return self.tree_library.search_by_title(title)
    
    def get_books_by_genre(self, genre):
        return self.tree_library.get_books_by_genre(genre)
    
    def get_all_books_alphabetical(self):
        return self.tree_library.inorder_traversal()

# Example usage if run directly
if __name__ == "__main__":
    library = BookHeapLibrary()
    
    # Add books to library with popularity scores
    library.add_book("1984", "George Orwell", 1949, ["dystopian", "political fiction"], 85)
    library.add_book("Brave New World", "Aldous Huxley", 1932, ["dystopian", "science fiction"], 75)
    library.add_book("The Hobbit", "J.R.R. Tolkien", 1937, ["fantasy"], 95)
    library.add_book("Animal Farm", "George Orwell", 1945, ["political fiction", "satire"], 70)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960, ["fiction", "classic"], 90)
    library.add_book("Pride and Prejudice", "Jane Austen", 1813, ["romance", "classic"], 80)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, ["fiction", "classic"], 65)
    
    # Simulate some book checkouts
    for _ in range(10):
        library.checkout_book("The Hobbit")
    
    for _ in range(5):
        library.checkout_book("1984")
    
    for _ in range(3):
        library.checkout_book("Pride and Prejudice")
    
    # Using heap operations
    print("Least popular books (for promotion):")
    least_popular = library.get_least_popular_books(3)
    for book in least_popular:
        print(f"  {book['title']} - Popularity: {book['popularity']}")
    
    print("\nMost popular books (for recommendations):")
    most_popular = library.get_most_popular_books(3)
    for book in most_popular:
        print(f"  {book['title']} - Popularity: {book['popularity']}")
    
    print("\nOldest books in the library:")
    oldest_books = library.get_oldest_books(3)
    for book in oldest_books:
        print(f"  {book['title']} ({book['year']}) by {book['author']}")
    
    print("\nMost frequently checked out books:")
    checkout_leaders = library.get_most_checked_out_books(3)
    for book in checkout_leaders:
        print(f"  {book['title']} - Checked out {book['checkout_count']} times")
    
    # Using tree operations
    print("\nBooks by genre (classic):")
    classics = library.get_books_by_genre("classic")
    print(f"  {classics}")
    
    print("\nAll books in alphabetical order:")
    all_books = library.get_all_books_alphabetical()
    for book in all_books:
        print(f"  {book['title']} ({book['year']}) by {book['author']}")
