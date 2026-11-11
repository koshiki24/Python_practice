'''8. Inventory Management System
Problem

Create product inventory software.

Requirements

Each product should contain:

product id
product name
quantity
price
Functionalities
Add stock
Reduce stock after purchase
Prevent negative stock
Calculate inventory value
Concepts Practiced
arithmetic inside classes
validations
inventory logic'''

class Inventory:
    def __init__(self,id,name,quantity,price):
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def add_stock(self):
        stock = int(input("Enter how much stock you want to add :"))
        if stock > 0:
            self.__quantity += stock
            print("Stock added successfully!!")
        else:
            print("Add valid stock!!")
    

    def reduce_stock(self):
        stock = int(input("Enter how much product you want to buy :"))
        if stock > 0 and stock <= self.__quantity:
            self.__quantity -= stock
            print("Stock purchased successfully!!")
        else:
            print("Product is not available!!")

    def inventory_value(self):
        value = self.__quantity * self.__price
        print(f"Total value is : {value}")

    def display(self):
        print(f"Id : {self.__id}\nName : {self.__name}\nQuantity : {self.__quantity}\nPrice : {self.__price}")

i1 = Inventory(101,"Biscuit",10,10)
i1.add_stock()
i1.display()
i1.reduce_stock()
i1.display()
i1.inventory_value()