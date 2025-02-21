class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        #TODO: use self.books's append method and pass in book as the append method's only argument
        pass  #TODO: remove when done.

    def remove_book(self, book):
        #TODO: use self.books's remove method and pass in book as the append method's only argument
        pass  #TODO: remove when done.

    def list_books(self):
        #TODO: need a for loop
        for book in self.books:
            #TODO: print out f"{book.title} by {book.author}
            pass  # TODO: remove when done.


my_library = Library()

book_0 = Book("To Kill a Mockingbird", "Harper Lee")
book_1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
my_library.add_book(book_0)
my_library.add_book(book_1)
my_library.list_books()