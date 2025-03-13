# library management system: protect book and user data 
#  have a look for the getter and settere function.
class Book:
    def __init__(self,title,author,isbn,copies):
        
        self.__title = title
        self.__author =author
        self.__isbn = isbn
        self.__copies =copies

        # getter function to acces the attributes of book class:

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_copies(self):
        return self.__copies
    
    # Setter method to update copies

    def set_copies(self,copies):
        if copies >= 0:
            self.__copies = copies
        else:
            print("copies can't be negative")

    def display_book(self):
        print(f"Title: {self.__title},\n Author: {self.__author},\n ISBN: {self.__isbn}, \n Copies Available: {self.__copies}")



#  Testing Encapsulation
book1 = Book("Experiment with Truth", "Mahatma Gandhi", "123456", 5)
book1.display_book()

# Direct access (❌ Not Allowed)
# print(book1.__title)  # AttributeError  Directly we can't access:
print(f" with the help of the getter function: {book1.get_title()}")  # Because it is private attribute we can access with th ehelp of the getter function.
# Correct access via getter (Allowed)


# # Modifying private attributes using setter
book1.set_copies(12)
print("Updated Copies:", book1.get_copies())  # Output: Updated Copies: 5




