class Book:

    def __init__(self, title, author, ISBN, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.availability_status = True

    def check_book(self): #checking book is available or not
        if self.availability_status:
            return "Available"
        else:
            return "Not available"

    def set_availability(self, status): #it changes status wwhich come from user class
        self.availability_status = status

    def get_details(self):
        details =  f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nAvailability: {self.check_book()}"
        if self.publication_date:
            details += f"\nPublication Date: {self.publication_date}"
            return details