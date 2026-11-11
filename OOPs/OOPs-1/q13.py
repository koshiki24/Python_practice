'''Write a Java program to create a class called "Inventory" with a collection of products and methods to add and remove products, and to check for low inventory.
'''

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        number = int(input("Enter how many product you want to add :"))
        
       
        for i in range(number):
            product_name = input("Enter product :")
            if product_name in self.products:
                self.products[product_name]+=1
            else:
                self.products[product_name] = 1

        print(f"{self.products}")

    def remove_product(self):
        product = input("Enter product you want to remove :")
        if product in self.products:
            self.products[product]-=1

            if self.products[product] == 0:
                del self.products[product]
        else:
            print("Product not found")

    def low_inventory(self):
        for key, value in self.products.items():
            if value < 2:
                print(f"{key} has low inventory : only {value}")

            

    def display(self):
        print(f"Products are : {self.products}")

i1 = Inventory()
i1.add_product()
i1.remove_product()
i1.display()
i1.low_inventory()
