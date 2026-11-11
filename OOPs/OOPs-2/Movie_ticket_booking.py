'''6. Movie Ticket Booking System
Problem

Create a movie booking system.

Requirements

Each movie should have:

movie name
total seats
available seats
Functionalities
Book tickets
Cancel tickets
Prevent overbooking
Display seat availability
Concepts Practiced
state updates
validations
object behavior'''

class Movie:
    def __init__(self,movie_name,total_seat,available_seat):
        self.__movie_name = movie_name
        self.__total_seat = total_seat
        self.__available_seat = available_seat

    def book_tickets(self):
        if self.__available_seat > 0:
            print("Ticket is booked!")
            self.__available_seat-=1
        else:
            print("There is no available seat!")

    def cancel_ticket(self):
        if self.__available_seat < self.__total_seat:
            print("Ticket canceled successfully!")
            self.__available_seat+=1
        else:
            print("There is no booking for this seat")

    def display_availability(self):
        print(f"Seat Available : {self.__available_seat}")

m1 = Movie("Dhurandar",2,2)
m2 = Movie("Mirzapur",10,1)
m1.display_availability()
#m2.display_availability()
m1.book_tickets()
m1.book_tickets()
m1.cancel_ticket()
m1.display_availability()
m2.display_availability()
m2.book_tickets()
m2.book_tickets()
m2.cancel_ticket()
m2.book_tickets()
# m1.display_availability()
# m2.display_availability()