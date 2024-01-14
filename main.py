from library_book_data import library  # Assuming library is a list of dictionaries with book data
from book import Book
from library import Library
from users import User  # Assuming you have a User class

# Load book data from the library_book_data module
book_data = library

# Create Book instances from the loaded data
books = [Book(item["title"], item["author"], item["ISBN"], item["publication_year"]) for item in book_data]

# Create a Library instance and add books to it
library_instance = Library()
for book in books:
    library_instance.add_book(book)

# Display available books in the library
print("Available Books in the Library:")
print(library_instance.display_available_books())

# Initialize current_user to None
current_user = None

# Main menu functions
def display_menu():
    print("\nLibrary System Menu:")
    print("1. View Available Books")
    print("2. Log In")
    print("3. View Borrowed Books")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Exit")

def run():
    global current_user  # Make current_user a global variable

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # View Available Books
            print(library_instance.display_available_books())
        elif choice == "2":
            # Log In
            user_name = input("Enter your name: ")
            user_id = input("Enter your user ID: ")
            current_user = User(user_name, user_id, book)  # Assuming User class takes name and user_id as parameters
            print(f"User {current_user.name} logged in.")
        elif choice == "3":
            # View Borrowed Books
            if current_user:
                print(current_user.view_borrowed_books())
            else:
                print("Please log in first.")
        elif choice == "4":
            # Borrow a Book
            if current_user:
                book_to_borrow = input("Enter the title of the book you want to borrow: ")
                # Implement borrowing logic here
                current_user.borrowing_book(book_to_borrow)
            else:
                print("Please log in first.")
        elif choice == "5":
            # Return a Book
            if current_user:
                book_to_return = input("Enter the title of the book you want to return: ")
                # Implement returning logic here
                current_user.returned_book(book_to_return)
            else:
                print("Please log in first.")
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run()




