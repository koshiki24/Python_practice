'''Write a Java program to create a class called "Employee" with a name, job title, and salary attributes, and methods to calculate and update salary.
'''

class Employee:
    def __init__(self,name,job_title,salary):
        self.__name = name
        self.__job_title = job_title
        self.__salary = salary

    def calculate_salary(self,percentage):
        increment = self.__salary * percentage/100
        return self.__salary + increment

    def update_salary(self,new_salary):
        self.__salary = new_salary
        print("SalaryUpdated")

    def display(self):
        print(f"Employee's name : {self.__name}, Job : {self.__job_title}, Salary : {self.__salary}")

e1 = Employee("Koshiki","AI Engineer",100000)
e1.display()
e1.update_salary(500000)
e1.display()