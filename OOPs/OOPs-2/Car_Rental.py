'''12. Car Rental System
Problem

Create a car rental platform.

Requirements

Each car:

car number
model
rental price per day
availability
Functionalities
Rent car
Return car
Calculate rent amount
Prevent renting unavailable cars'''

class Car:
    def __init__(self,car_no,model,rental_price_per_day,availability):
        self.__car_no = car_no
        self.__model = model
        self.__rental_price_per_day = rental_price_per_day
        self.__availability = availability

    def rent_car(self):
        days = int(input("Enter for how many days you want to rent a car :"))
        if self.__availability == True:
            self.__availability = False
            rent_amount = self.__rental_price_per_day * days
            print("Car rented successful!")
            print(f"Car Model : {self.__model}")
            print(f"Car Number : {self.__car_no}")
            print(f"Car price per day : {self.__rental_price_per_day}")
            print(f"Total amount : {rent_amount}")

        else:
            print("Sorry! This car is not available for rent")

    def return_car(self):
        if self.__availability == False:
            self.__availability = True
            print("Car returned successful!")

        else:
            print("This car was not in rented")

    def display(self):
        print(f"Car Details\nCar Model : {self.__model}\nCar Number : {self.__car_no}\nCar Rental Price Per Day : {self.__rental_price_per_day}")

        if self.__availability:
            print("Availability : Available")
        else:
            print("Availability : Not Available")

c1 = Car("MP13 AB 1234", "Swift", 1500, True)
c2 = Car("MP13 AQ 0470", "WagonR",1000,True)
c1.rent_car()
c1.display()
print("\n")
c2.return_car()
c2.display()


