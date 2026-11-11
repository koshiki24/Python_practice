'''19. Flight Reservation System
Problem

Create airline reservation software.

Requirements

Flight should contain:

flight number
total seats
booked seats
Functionalities
Book ticket
Cancel ticket
Prevent overbooking'''

class Flight:
    def __init__(self,flight_number,total_seat):
        self.__flight_number = flight_number
        self.__total_seat = total_seat
        self.__booked_seat = 0

    def book_ticket(self,seat):
        if seat <= 0:
            print("No seat found")
        elif self.__booked_seat + seat <= self.__total_seat:
            self.__booked_seat += seat
            print(seat,"Booked successfully")
        else:
            print("Sorry Not enough seat available")
    def cancel_ticket(self,seat):
        if seat <= 0:
            print("Please enter a valid number of seat")
        elif seat <= self.__booked_seat:
            self.__booked_seat -= seat
            print(seat,"Ticket cancelled successfully!")
        else:
            print("Invalid cancellation!No such booking exists")
    def display(self):
        available_seats = self.__total_seat - self.__booked_seat

        print("\n------ Flight Details ------")
        print("Flight Number:", self.__flight_number)
        print("Total Seats:", self.__total_seat)
        print("Booked Seats:", self.__booked_seat)
        print("Available Seats:", available_seats)

f1 = Flight("AI202", 100)
f2 = Flight("6E305", 50)

# Booking tickets
f1.book_ticket(20)
f1.book_ticket(30)

# Display flight details
f1.display()

# Cancelling tickets
f1.cancel_ticket(10)

# Display updated details
f1.display()

# Trying to overbook
f1.book_ticket(100)

# Display another flight
f2.display()






# class Flight:
#     def __init__(self, flight_number, total_seats):
#         self.__flight_number = flight_number
#         self.__total_seats = total_seats
#         self.__booked_seats = 0

#     def book_ticket(self, seats):
#         if seats <= 0:
#             print("Please enter a valid number of tickets.")

#         elif self.__booked_seats + seats <= self.__total_seats:
#             self.__booked_seats += seats
#             print(seats, "ticket(s) booked successfully!")

#         else:
#             print("Sorry! Not enough seats available.")

#     def cancel_ticket(self, seats):
#         if seats <= 0:
#             print("Please enter a valid number of tickets.")

#         elif seats <= self.__booked_seats:
#             self.__booked_seats -= seats
#             print(seats, "ticket(s) cancelled successfully!")

#         else:
#             print("Invalid cancellation! No such booking exists.")

#     def display_details(self):
#         available_seats = self.__total_seats - self.__booked_seats

#         print("\n------ Flight Details ------")
#         print("Flight Number:", self.__flight_number)
#         print("Total Seats:", self.__total_seats)
#         print("Booked Seats:", self.__booked_seats)
#         print("Available Seats:", available_seats)


# # Creating objects
# f1 = Flight("AI202", 100)
# f2 = Flight("6E305", 50)

# # Booking tickets
# f1.book_ticket(20)
# f1.book_ticket(30)

# # Display flight details
# f1.display_details()

# # Cancelling tickets
# f1.cancel_ticket(10)

# # Display updated details
# f1.display_details()

# # Trying to overbook
# f1.book_ticket(100)

# # Display another flight
# f2.display_details()
