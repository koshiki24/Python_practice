'''14. Restaurant Billing System
Problem

Create restaurant order system.

Requirements

Each order:

table number
ordered items
prices
Functionalities
Add items
Remove items
Calculate total bill
Add service tax using static method'''

class Restaurant:
    def __init__(self,table_number):
        self.__table_number = table_number
        self.__ordered_items = {}

    def add_item(self,item,price):
        self.__ordered_items[item] = price
        print(item,"added successfully")

    def remove_item(self,item):
        if item in self.__ordered_items:
            del self.__ordered_items[item]
            print(item,"removed successfully")
        else:
            print(item,"not found")

    @staticmethod
    def add_service_tax(total):
        return total *5/100


    def calculate_bill(self):
        total = 0
        print("----------------Restaurant Bill---------------")
        print(f"Table Number :{self.__table_number}")
        for item,price in self.__ordered_items.items():
            print(item,":",price)
            total += price

            print(f"Total Amount : {total}")

            service_tax = Restaurant.add_service_tax(total)

            print(f"Service Tax : {service_tax}")
            print(f"Final Bill : {total + service_tax}")

r1 = Restaurant(5)
r1.add_item("Pizza",250)
r1.add_item("Burger",200)
r1.add_item("Pasta",300)
r1.remove_item("Burger")
r1.calculate_bill()