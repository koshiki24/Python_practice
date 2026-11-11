'''Write a Java program to create a class called "Book" with attributes for title, author, and ISBN, and methods to add and remove books from a collection.
'''

class Book:
    def __init__(self,title,author,ISBN):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
    def display(self):
        print(f"Title : {self.__title}, Author : {self.__author}, ISBN : {self.__ISBN}")
# b1 = Book("Python","Guido",101)
# b1.display()

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self,ISBN):
        for book in self.books:
            if book._Book__ISBN == ISBN:
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("book not found!")

    def display_book(self):
        if len(self.books) == 0:
            print("Collection is empty")
        else:
            for book in self.books:
                book.display()

b1 = Book("Python Programming","Guido",101)
b2 = Book("Java Programming","James",102)

collection = BookCollection()

collection.add_book(b1)
collection.add_book(b2)

print("\nBook Collections:")
#collection.display_book()

b3 = Book("C","Dennis Ritchie",103)
collection.add_book(b3)
#collection.display_book()

collection.remove_book(101)
collection.display_book()


    
