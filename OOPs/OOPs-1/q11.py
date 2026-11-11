'''Write a Java program to create a class called "Library" with a collection of books and methods to add and remove books.
'''

class Library:
    def __init__(self):
        self.books = {}

    def add_books(self,name,author,isbn):
        self.books[isbn] = {
            "name" : name,
            "author" : author
        }
        print("Book added successfully")

    def remove_book(self):
        isbn = input("Enter isbn which you want to remove :")
        if isbn in self.books:
            del self.books[isbn]
            print("Deleted successfully")
        else:
            print("Book not found")
    def display(self):
        print(self.books)
c1 = Library()

c1.add_books("Python","Guido","101")
c1.add_books("c","Ritchie",102)
c1.display()
c1.remove_book()



