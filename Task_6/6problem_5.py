class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print("Book borrowed successfully")
        else:
            print("Book is already borrowed")


book1 = Book("Python Basics", "Ali")

book1.borrow_book()
book1.borrow_book()