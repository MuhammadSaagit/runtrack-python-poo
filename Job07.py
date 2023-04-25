class Book:
    def __init__(self, title, author, num_pages):
        self.__title = title
        self.__author = author
        self.__num_pages = num_pages

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_num_pages(self):
        return self.__num_pages

    def set_num_pages(self, num_pages):
        if num_pages > 0:
            self.__num_pages = num_pages
        else:
            print("Error: Number of pages must be a positive integer.")


book = Book("Beyond Good and Evil", "Friedrich Nietzsche", 240)

print("Book title:", book.get_title())
print("Book author:", book.get_author())
print("Number of pages:", book.get_num_pages())

book.set_title("To Kill a Mockingbird")
book.set_author("Harper Lee")

book.set_num_pages(250)
print("Updated number of pages:", book.get_num_pages())

book.set_num_pages(-10)  # Should throw an error message
