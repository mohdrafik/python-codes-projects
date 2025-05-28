class Library:
    def __init__(self, num_books, books_name):
        self.books_name = books_name
        self.num_books = num_books

    # num_books = ()
    # books_name = []
    def print_info(self):
        # self.num_books = self.num_books
        print(self.num_books)
        print(len(self.books_name))

    def check_lennumof_books(self):
        if self.num_books == self.num_books:
            print("same ")
        else:
            print("no is not same")

    # def __init__(self):


books_name = ["algebra", "math", "science","jk"]
numofbooks = (len(books_name))
a = Library(numofbooks, books_name)
a.print_info()
a.check_lennumof_books()
