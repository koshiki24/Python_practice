'''Product Inventory
Create a class Product with fields: productId, name, quantity, price.
Use setters to assign values. Add a method to calculate total value (quantity * price).'''
class Product:

    def __init__(self):
        self.__productId = 0
        self.__name = ""
        self.__quantity = 0
        self.__price = 0.0

    # Setter methods
    def set_product_id(self, product_id):
        self.__productId = product_id

    def set_name(self, name):
        self.__name = name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    # Calculate total value
    def calculate_total_value(self):
        return self.__quantity * self.__price

    # Display product details
    def display(self):
        print("Product ID :", self.__productId)
        print("Product Name :", self.__name)
        print("Quantity :", self.__quantity)
        print("Price :", self.__price)
        print("Total Value :", self.calculate_total_value())


p1 = Product()

p1.set_product_id(101)
p1.set_name("Laptop")
p1.set_quantity(5)
p1.set_price(40000)

p1.display()