'''3. Online Shopping Cart
Problem

Create a shopping cart system.

Requirements

A cart should:

store customer name
maintain list of products
maintain total bill
Functionalities
Add product
Remove product
Calculate final amount
Apply discount using static method
Track total carts created
Concepts Practiced
list inside object
object interaction
static method
class variable'''

class Cart:
    product_list = {}
    total_carts = 0

    def __init__(self,customer_name):
        self.__customer_name = customer_name
        self.__total_bill = 0

        if customer_name not in Cart.product_list:
            Cart.product_list[customer_name] = []
            Cart.total_carts+=1

    def add_product(self):
        name = input("Enter product name :")
        price = float(input("Enter product price :"))
        Cart.product_list[self.__customer_name].append([name,price])
        print("Product added successfully!")
        

    def remove_product(self):
        product = input("Enter product name you want to remove :")
        for item in Cart.product_list[self.__customer_name]:
            if item[0] == product:
                Cart.product_list[self.__customer_name].remove(item)
                print("Product removed successfully!")
                return
            print("Product not found")

    def calculate_amount(self):
        self.__total_bill = 0
        for item in Cart.product_list[self.__customer_name]:
            self.__total_bill += item[1]
        return self.__total_bill

    @staticmethod
    def apply_discount(amount):
        if amount >=1000:
            return amount - (amount *10/100)
        return amount
c1 = Cart("Koshiki")
c1.add_product()
c1.add_product()

c2 = Cart("Shriya")
c2.add_product()
c2.add_product()

print("\nAll Customers :",Cart.product_list)
print("\nKoshiki's Bill:", c1.calculate_amount())
print("\nShriya's Bill :",c2.calculate_amount())

print("\nKoshiki's Final Amount :",Cart.apply_discount(c1.calculate_amount()))
print("\nShriya's Final Amount :",Cart.apply_discount(c2.calculate_amount()))

print("Total Carts credited:",Cart.total_carts)

        
        
        
