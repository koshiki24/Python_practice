'''Write a Java program to create a class called "Employee" with a name, salary, and hire date attributes, and a method to calculate years of service.
'''

class Employee:
    def __init__(self,name,salary,hire_day,hire_month,hire_year,current_day,current_month,current_year):
        self.__name = name
        self.__salary = salary
        #self.__hire_date = hire_date
        self.__hire_day = hire_day
        self.__hire_month = hire_month
        self.__hire_year = hire_year 
        self.__current_day = current_day
        self.__current_month = current_month
        self.__current_year = current_year 

    def calculate_years(self):
        if self.__current_year > self.__hire_year:
            years = self.__current_year - self.__hire_year
        if self.__hire_month > self.__current_month:
            years -=1
        return years

    def set_hire_year(self,hire_year):
        self.__hire_year = hire_year

    def get_hire_year(self):
        return self.__hire_year

    def display(self):
        print(f"Total year of working is : {self.calculate_years()}")

e1 = Employee("Shriya",50000,5,2,2011,31,10,2026)
e1.display()

e2 = Employee("A",10000,10,12,2021,5,2,2026)
e2.display()

e2.set_hire_year(2025)
e2.display()
print(e2.get_hire_year())



        
