class User():

    def __init__(self, name, id, book):
        self.book = book
        self.name = name
        self.id = id
        self.book_borrowed = []

    def borrowing_book(self, book):
        if self.book.check_book():
            self.book.set_availability(False)
            self.book_borrowed.append(book)
            return f"Book '{book.title}' has been borrowed successfully."
        else:
            return f"Book '{book.title}' is not available for borrowing."

    def returned_book(self, book):
        if book in self.book_borrowed:
            self.book.set_availability(True)
            self.book_borrowed.remove(book)
            return f"Book '{book.title}' has been returned successfully."
        else:
            return f"You didn't borrow the book '{book.title}'."

    def view_borrowed_books(self):
        if not self.book_borrowed:
            return "You haven't borrowed any books."
        else:
            borrowed_books = [book.title for book in self.book_borrowed]
            return f"You have borrowed the following books: {borrowed_books}"


