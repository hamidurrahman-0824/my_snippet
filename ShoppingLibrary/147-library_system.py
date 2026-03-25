"""OOP design
Data structures (dictionary / list)
State management (available vs borrowed)
Method design"""
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
class Library:
    
    def __init__(self):
        # books available in library
        self.books = {
            "Python": 5,
            "Algorithms": 3,
            "Data Science": 2,
            "Machine Learning": 4
        }
        
        # borrowed books by users
        self.borrowed = {}

    def show_books(self):
        """Display available books"""
        print("\nAvailable Books:")
        for book, qty in self.books.items():
            print(f"{book} : {qty}")

    def borrow_book(self, user, book):
        """Borrow a book"""
        if book not in self.books:
            print("Book not found in library.")
            return
        
        if self.books[book] == 0:
            print("Book currently unavailable.")
            return
        
        # reduce available count
        self.books[book] -= 1
        
        # add to borrowed list
        if user not in self.borrowed:
            self.borrowed[user] = []
        
        self.borrowed[user].append(book)
        
        print(f"{user} borrowed '{book}'")

    def return_book(self, user, book):
        """Return a book"""
        if user not in self.borrowed or book not in self.borrowed[user]:
            print("Return not valid.")
            return
        
        self.borrowed[user].remove(book)
        self.books[book] += 1
        
        print(f"{user} returned '{book}'")

    def user_books(self, user):
        """Show books borrowed by user"""
        if user in self.borrowed:
            print(f"{user} borrowed:", self.borrowed[user])
        else:
            print("No books borrowed.")