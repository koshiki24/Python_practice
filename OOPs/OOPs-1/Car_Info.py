'''Car Info Manager
Create a class Car with fields: brand, model, and year.
Use setters to assign values. Create a method to print full car info.'''

class Car:
    def __init__(self,branch,model,year):
        self.__branch = branch
        self.__model = model
        self.__year = year

    def set_branch(self,branch):
            self.__branch = branch
    
    def set_model(self,model):
            self.__model = model
    
    def set_year(self,year):
            self.__year = year
    
    def display(self):
            print(f"Branch : {self.__branch}\nModel : {self.__model}\nYear : {self.__year}")
    
c = Car("Ujjain",2021,2023)
c.display()
c.set_branch("Indore")
c.set_model(2024)
c.set_year(2026)
c.display()

    