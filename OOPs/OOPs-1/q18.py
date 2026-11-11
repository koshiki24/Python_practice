'''Write a Java program to create a class called "Restaurant" with attributes for menu items, prices, and ratings, and methods to add and remove items, and to calculate average rating.
'''

class Restaurant:

    def __init__(self):
        self.menu = {}
        self.ratings = []

    def add_item(self):
        items = input("Enter item :")
        price = int(input("Enter price :"))

        self.menu[items] = price
        #print("Item added successfully!")

    def remove_item(self):
        item = input("Enter item you want to remove :")
        if item in self.menu:
            del self.menu[item]
            #print("Item removed successfully!")
        else:
            print("Item not found")

    def add_rating(self):
        rating = int(input("Enter rating between (1-5) : "))
        if rating>=1 and rating<=5:
            self.ratings.append(rating)
            #print("Rating added successfully!")
        else:
            print("Invalid rating")

    def average_rating(self):
        if len(self.ratings) > 0:
            average = sum(self.ratings)/len(self.ratings)
            #print(f"Average rating : {average}")
            return average
        else:
            return 0

    def display(self):
        print(f"Menu are : {self.menu}")
        print(f"Ratings are : {self.ratings}")
        print(f"Average rating is : {self.average_rating()}")


r = Restaurant()
r.add_item()
r.add_item()
r.add_item()
r.add_rating()
r.add_rating()
r.add_rating()
r.display()




