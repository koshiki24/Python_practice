'''10. Company Department System
Problem

Create:

Department
Employee

classes.

Requirements

Each department:

has department name
stores employee objects
Functionalities
Add employee to department
Display all employees
Calculate total department salary
Concepts Practiced
object composition
object interaction
storing objects in lists'''
class Employee:
    def __init__(self,emp_id,emp_name,salary):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display_employee(self):
        print(f"Employee Id : {self.__emp_id}\nEmployee Name : {self.__emp_name}\nEmployee Salary : {self.__salary}")

class Department:
    def __init__(self,department_name):
        self.__department_name = department_name
        self.employee = []

    def add_employee(self,employee):
        self.employee.append(employee)
        print("Employee added successfully!")

    def display_employee(self):
        print("\nDepartment Name :", self.__department_name)
        print("\nEmployee Details")

        if len(self.employee) == 0:
            print("No employee found!")

        else:
            for employee in self.employee:
                employee.display_employee()
                print("----------")

    def total_salary(self):
        total = 0

        for employee in self.employee:
            total += employee.get_salary()

        print("Total Employee Salary :",total)

e1 = Employee(101,"koshiki",1000000)
e2 = Employee(102,"Shriya",1000000)
e3 = Employee(103,"Divya",100000)

d1 = Department("IT")
d1.add_employee(e1)
d1.add_employee(e2)
d1.add_employee(e3)
d1.display_employee()

d1.total_salary()
