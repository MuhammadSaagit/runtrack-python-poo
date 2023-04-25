class Book:
    def __init__(self, title, author, num_pages):
        self.__title = title
        self.__author = author
        self.__num_pages = num_pages
        self.__available = True

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

    def __str__(self):
        return f"{self.__title} by {self.__author}, {self.__num_pages} pages"

    def check(self):
        return self.__available

    def borrow(self):
        if self.check():
            self.__available = False
            print("Book borrowed successfully!")
        else:
            print("The book is already borrowed.")

    def return_book(self):
        if not self.check():
            self.__available = True
            print("Book returned successfully!")
        else:
            print("The book is already available.")

    def return_book(self):
        if not self.check():
            self.__available = True
            print("Book returned successfully!")
        else:
            print("The book is already available.")

    def borrow_and_return(self):
        if self.check():
            self.borrow()
            self.return_book()
        else:
            print("The book is already borrowed.")


# Example usage
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 234)
book2 = Book("Sun Tzu's Art Of War", "Sun Tzu", 152)

book1.borrow_and_return()
book2.borrow_and_return()
