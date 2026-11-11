'''Write a Java program to create a class called "Dog" with a name and breed attribute. Create two instances of the "Dog" class, set their attributes using the constructor and modify the attributes using the setter methods and print the updated values.
'''

class Dog:
    def __init__(self,name,breed):
        self.__name = name
        self.__breed = breed
    def set_name(self,name):
        self.__name = name
    def set_breed(self,breed):
        self.__breed = breed
    def get_name(self):
        return self.__name
    def get_breed(self):
        return self.__breed
    def display(self):
        print(f"Name : {self.__name} , Breed : {self.__breed}")

dog1 = Dog("Tommy", "Labrador")
dog2 = Dog("Bruno","German Shepherd")
dog1.display()
dog2.display()

dog1.set_name("Rocky")
dog1.set_breed("Pomerianian")

dog2.set_name("Max")
dog2.set_breed("Pug")

dog1.display()
dog2.display()