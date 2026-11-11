'''1. Write a Python program to create a class called "Person" with a name and age attribute. Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.'''

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def display(self):
        print(f"Name : {self.__name}\nAge : {self.__age}")
p1 = Person("Koshiki",21)
p2 = Person("Shriya",16)
p1.display()
p2.display()

