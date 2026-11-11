'''11. E-Commerce Product System
Problem

Create product system for online store.

Requirements

Each product should have:

product name
price
category
Functionalities
Apply GST using static method
Apply category discount
Display final price
Concepts Practiced
static methods
calculations
reusable logic'''

class Product:
    def __init__(self,product_name,price,category):
        self.__product_name = product_name
        self.__price = price
        self.__category = category

    @staticmethod
    def gst(price):
        gst = price * 18/100
        return gst

    def discount(self):
        if self.__category == "Electronics":
            discount = self.__price * 10/100
        elif self.__category == "Clothing":
            discount = self.__price * 20/100
        elif self.__category == "Food":
            discount = self.__price*25/100
        else:
            discount = self.__price *5/100
        return discount

    def display(self):
        gst = Product.gst((self.__price))
        discount = self.discount()
        final_price = self.__price + gst - discount

        print(f"Product Name : {self.__product_name}\nPrice : {self.__price}\nCategory : {self.__category}\nGST : {gst}\nDiscount : {discount}\nFinal Price : {final_price}")

p1 = Product("Laptop",50000,"Electronics")
p2 = Product("Shirt",1000,"Clothing")
p3 = Product("Pizza",500,"Food")

p1.display()
p2.display()
p3.display()


