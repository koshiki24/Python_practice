'''Employee Record System
Create a class Employee with private fields: id, name, and salary.
Use setter methods to assign values. Add a method to display employee details.
'''

class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def set_id(self,id):
        self.__id = id

    def set_name(self,name):
        self.__name = name

    def set_salary(self,salary):
        self.__salary = salary

    def display(self):
        print(f"Id : {self.__id}\nName : {self.__name}\nSalary : {self.__salary}")

e = Employee(1,"Koshiki",100000)
e.display()
e.set_name("Shriya")
e.set_salary(500000)
e.display()