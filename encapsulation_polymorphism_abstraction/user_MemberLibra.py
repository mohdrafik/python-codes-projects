from book_data import Book

# Parent Class

class User:
    def __init__(self, name, user_id):
        self._name = name       # Protected Attribute
        self._user_id = user_id # Protected Attribute

    def display_user(self):
        print(f"User ID: {self._user_id}, Name: {self._name}")

# Child Class - Member
class Member(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.__borrowed_books = []  # Private Attribute

    def borrow_book(self, book):
        if book.get_copies() > 0:
            self.__borrowed_books.append(book.get_title())
            book.set_copies(book.get_copies() - 1)
            print(f"{self._name} borrowed {book.get_title()}.")
        else:
            print(f"Sorry, {book.get_title()} is not available.")

    def display_user(self):
        super().display_user()
        print(f"Borrowed Books: {self.__borrowed_books}")

# Child Class - Librarian
class Librarian(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def add_book(self, book, copies):
        book.set_copies(book.get_copies() + copies)
        print(f"{copies} copies of '{book.get_title()}' added by Librarian {self._name}.")


# Testing Inheritance
member1 = Member("Alice", 101)
librarian1 = Librarian("Mr. Smith", 201)

book2 = Book("1984", "George Orwell", "0987654321", 2)
librarian1.add_book(book2, 3)
member1.borrow_book(book2)
member1.display_user()
