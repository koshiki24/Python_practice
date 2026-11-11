'''5. Library Management System
Problem

Design a library system.

Requirements

Each book should contain:

book id
title
author
availability status
Functionalities
Issue book
Return book
Display availability
Count total books using class variable
Additional Challenge

Prevent issuing already issued books.

Concepts Practiced
object state changes
boolean flags
class variables'''
class Library:
    total_books = 0
    def __init__(self,id,title,author,availability):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__availability = availability

        Library.total_books+=1

    def issue_book(self):
        if self.__availability == True:
            self.__availability = False
            print(f"Book Issued successfully!")
        else:
            print("Book is already issued!")

    def return_book(self):
        if self.__availability == False:
            self.__availability = True
            print("Book Return Successfully!")
        else:
            print("Book already returned!")

    def display(self):
        print(f"Book ID : {self.__id}\nTitle : {self.__title}\nAuthor : {self.__author}\nAvailability : {self.__availability}")

    @classmethod
    def count(cls):
        print(f"Total Books : {Library.total_books}")

b1 = Library(101,"Python","Guido",False)
b2 = Library(102,"C","Ritchie",True)

b1.issue_book()
b1.return_book()
b1.display()

b2.issue_book()
b2.return_book()
b2.display()

Library.count()


