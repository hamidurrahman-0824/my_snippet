class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class ShoppingCart:
    def __init__(self):
        # Using dictionary to hold the items and quantities in cart
        self.items = {}  # {'book1': 2, 'book2': 3} etc.
    
    def add_book(self, book, quantity=1):
        if not isinstance(book, Book):
            raise ValueError("Expecting an instance of Book")
        
        # If the book already exists in cart, increment its quantity
        if book.title in self.items:
            self.items[book.title] += quantity
        else: 
            self.items[book.title] = quantity
    
    def remove_book(self, book):
        # Check if the given item is a Book instance and exists in cart
        if not isinstance(book, Book) or book.title not in self.items:
            raise ValueError("Book does not exist in the shopping cart")
        
        del self.items[book.title]  # Remove from cart
    
    def total_cost(self):
        total = 0
        items = {'fish': 2,'pen': 3}  # 'dalim' was removed as it doesn't exist in this dictionary
        
        for book, quantity in self.items.items():
            if book in items:
                total += quantity * items[book]
                
        return total
