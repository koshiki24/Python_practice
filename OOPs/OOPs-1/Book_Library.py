'''Book Library
Create a class Book with fields: title, author, and price.
Use setters to assign values and a method to print book details.'''

class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self,title):
        self.__title = title

    def set_author(self,author):
            self.__author = author

    def set_price(self,price):
            self.__price = price

    def display(self):
          print(f"Title : {self.__title}\nAuthor : {self.__author}\nPrice : {self.__price}")

b = Book("Python","Guido",500)
b.display()
b.set_author("Rossom")
b.set_title("c")
b.set_price(500)
b.display()

