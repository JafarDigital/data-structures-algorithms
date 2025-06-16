"""
TREES
Trees are hierarchical data structures that consist of nodes connected by edges, with one node designated as the root. Unlike linear data structures like arrays or linked lists, trees allow for representing hierarchical relationships between elements
Intuitive easy way to understand trees is as folders and files.

"""

from collections import deque

class BookNode:
    def __init__(self, title, author, year, popularity=0):
        self.title = title
        self.author = author
        self.year = year
        self.popularity = popularity
        self.left = None
        self.right = None
        self.height = 1  # For AVL tree balancing

class BookTreeLibrary:
    def __init__(self):
        self.root = None
        self.genre_index = {}  # Maps genre to list of books
    
    def add_book(self, title, author, year, genres, popularity=0):
        # Add to AVL tree (balanced BST organized by title)
        self.root = self._insert_avl(self.root, title, author, year, popularity)
        
        # Add to genre index
        for genre in genres:
            if genre not in self.genre_index:
                self.genre_index[genre] = []
            self.genre_index[genre].append(title)
        
        return {"title": title, "author": author, "year": year, "popularity": popularity}
    
    def _insert_avl(self, root, title, author, year, popularity):
        # Standard BST insert
        if not root:
            return BookNode(title, author, year, popularity)
        
        if title < root.title:
            root.left = self._insert_avl(root.left, title, author, year, popularity)
        else:
            root.right = self._insert_avl(root.right, title, author, year, popularity)
        
        # Update height
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        
        # Get balance factor
        balance = self._get_balance(root)
        
        # Perform rotations if needed to balance the tree
        
        # Left heavy
        if balance > 1:
            # Left-Right case
            if title > root.left.title:
                root.left = self._left_rotate(root.left)
            # Left-Left case
            return self._right_rotate(root)
        
        # Right heavy
        if balance < -1:
            # Right-Left case
            if title < root.right.title:
                root.right = self._right_rotate(root.right)
            # Right-Right case
            return self._left_rotate(root)
        
        return root
    
    def search_by_title(self, title):
        return self._search_recursive(self.root, title)
    
    def _search_recursive(self, node, title):
        if node is None:
            return None
        
        if title == node.title:
            return {"title": node.title, "author": node.author, "year": node.year, "popularity": node.popularity}
        elif title < node.title:
            return self._search_recursive(node.left, title)
        else:
            return self._search_recursive(node.right, title)
    
    def get_books_by_genre(self, genre):
        return self.genre_index.get(genre, [])
    
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _right_rotate(self, y):
        x = y.left
        T3 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T3
        
        # Update heights
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        
        return x
    
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    # ---- TREE TRAVERSAL METHODS ----
    
    def inorder_traversal(self):
        """Left-Root-Right: gives alphabetically sorted books"""
        books = []
        self._inorder(self.root, books)
        return books
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append({
                "title": node.title, 
                "author": node.author, 
                "year": node.year,
                "popularity": node.popularity
            })
            self._inorder(node.right, result)
    
    def preorder_traversal(self):
        """Root-Left-Right: useful for reconstructing the tree"""
        books = []
        self._preorder(self.root, books)
        return books
    
    def _preorder(self, node, result):
        if node:
            result.append({
                "title": node.title, 
                "author": node.author, 
                "year": node.year,
                "popularity": node.popularity
            })
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def postorder_traversal(self):
        """Left-Right-Root: useful for deletion"""
        books = []
        self._postorder(self.root, books)
        return books
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append({
                "title": node.title, 
                "author": node.author, 
                "year": node.year,
                "popularity": node.popularity
            })
    
    def level_order_traversal(self):
        """Breadth-first traversal: visit books level by level"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append({
                "title": node.title, 
                "author": node.author, 
                "year": node.year,
                "popularity": node.popularity
            })
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

# Example usage if run directly
if __name__ == "__main__":
    library = BookTreeLibrary()
    
    # Add books to library
    library.add_book("1984", "George Orwell", 1949, ["dystopian", "political fiction"], 85)
    library.add_book("Brave New World", "Aldous Huxley", 1932, ["dystopian", "science fiction"], 75)
    library.add_book("The Hobbit", "J.R.R. Tolkien", 1937, ["fantasy"], 95)
    
    # Search for a book
    book = library.search_by_title("The Hobbit")
    print(f"Found book: {book}")
    
    # Get books by genre
    dystopian_books = library.get_books_by_genre("dystopian")
    print(f"Dystopian books: {dystopian_books}")
    
    # Show different traversals
    print("\nBooks in alphabetical order (inorder traversal):")
    for book in library.inorder_traversal():
        print(f"  {book['title']} ({book['year']}) by {book['author']}")
