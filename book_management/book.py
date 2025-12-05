class Book:  
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Book: [ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}]")