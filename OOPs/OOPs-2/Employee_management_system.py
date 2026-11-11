'''1. Employee Management System
Problem

Create an Employee class to manage employee details.

Requirements

Each employee should have:

employee id
name
department
salary
Functionalities
Display employee details
Increase salary by percentage
Count total employees created using a class variable

Create employee object from a string:

"101-Rahul-IT-50000"

using a class method.

Concepts Practiced
constructor
instance variables
class variables
class method
instance methods'''

class Employee:
    __counter = 0

    def __init__(self,id,name,department,salary):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__salary = salary
        Employee.__counter+=1

    def display(self):
        print(f"Id : {self.__id}\nName : {self.__name}\nDepartment : {self.__department}\nSalary : {self.__salary}")

    def increase_salary(self,per):
        self.__salary = self.__salary + (self.__salary * per)/100

    @classmethod
    def from_employees(cls,emp_details):
        id,name,department,salary = emp_details.split("-")
        return cls(id,name,department,float(salary))

    @classmethod
    def get_counter(cls):
        return cls.__counter

emp = Employee.from_employees("101-Koshiki-CSE-100000")
emp.display()

emp.increase_salary(10)
emp.display()
print(f"Total object created : {Employee.get_counter()}")

