'''Mobile Phone Store
Create a class Mobile with fields: brand, model, price.
Use setters to set values. Create a method to check if phone is affordable (price < 20000).
'''

class Mobile:

    def __init__(self):
        self.__brand = ""
        self.__model = ""
        self.__price = 0.0

    # Setter methods
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    # Check affordability
    def is_affordable(self):
        if self.__price < 20000:
            return True
        else:
            return False

    # Display mobile details
    def display(self):
        print("Brand :", self.__brand)
        print("Model :", self.__model)
        print("Price :", self.__price)

        if self.is_affordable():
            print("Phone is affordable")
        else:
            print("Phone is not affordable")


m1 = Mobile()

m1.set_brand("OnePlus")
m1.set_model("Nord CE 3 Lite")
m1.set_price(18000)

m1.display()