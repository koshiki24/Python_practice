'''Write a Java program to create a class called "Movie" with attributes for title, director, actors, and reviews, and methods for adding and retrieving reviews.
'''

class Movie:
    def __init__(self,title,director,actors):
        self.__title = title
        self.__director = director
        self.__actors = actors
        self.reviews = []

    def add_review(self):
        review = input("Enter review :")
        self.reviews.append(review)

    def retrieve_review(self):
        for review in self.reviews:
            print(review)

m = Movie("3 Idiots","Rajkumar Hirani",["Amir Khan","R Madhavan","Sharman Joshi"])

m.add_review()
m.add_review()
print("Movie Review")
m.retrieve_review()
