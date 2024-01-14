class Library():

    def __init__(self):
        self.books = []
        self.users = []

    def display_available_books(self):
        # Iterate through books and check availability
        available_books = [book.get_details() for book in self.books if book.check_book()]
        if not available_books:
            return "No books are available in the library."
        else:
            return "\n".join(available_books)

    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book.title}' has been added to the library."

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"Book '{book.title}' has been removed from the library."
        else:
            return f"Book '{book.title}' is not in the library."
