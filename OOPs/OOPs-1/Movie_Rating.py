'''Movie Rating System
Create a class Movie with fields: name, genre, and rating.
Use setters and create a method isHit() that returns true if rating ≥ 8.0.
'''

class Movie:

    def __init__(self):
        self.__name = ""
        self.__genre = ""
        self.__rating = 0.0

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_genre(self, genre):
        self.__genre = genre

    def set_rating(self, rating):
        self.__rating = rating

    # Check whether movie is a hit
    def isHit(self):
        if self.__rating >= 8.0:
            return True
        else:
            return False

    # Display movie details
    def display(self):
        print("Movie Name :", self.__name)
        print("Genre :", self.__genre)
        print("Rating :", self.__rating)

        if self.isHit():
            print("Movie Status : Hit")
        else:
            print("Movie Status : Not a Hit")


m1 = Movie()

m1.set_name("3 Idiots")
m1.set_genre("Comedy Drama")
m1.set_rating(8.4)

m1.display()