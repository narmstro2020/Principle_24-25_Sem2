class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        #TODO: append to self.books the book.
        pass #TODO: remove when done

    def remove_book(self, book):
        #TODO: remove from self.books the book
        pass #TODO: remove when done

    def list_books(self):
        #TODO: make a for loop, for book in self.books
        #TODO: inside the for loop's block print
        #TODO: f"{book.title} by {book.author}
        pass #TODO: remove when done

my_library = Library()
my_book_1 = Book("To Kill a Mockingbirg", "Harper Lee")
my_book_2 = Book("Silent Spring", "Rachel Carson")
my_library.add_book(my_book_1)
my_library.add_book(my_book_2)
my_library.list_books()
