'''16. Train Reservation System
Problem

Design ticket reservation system.

Requirements

Train should contain:

train number
total seats
booked seats
Functionalities
Reserve seat
Cancel seat
Display available seats'''


class Train:
    def __init__(self,train_number,total_seat):
        self.__train_number = train_number
        self.__total_seat = total_seat
        self.__booked_seat = 0

    def reserve_seat(self):
        seat = int(input("Enter seat number :"))
        if seat < 0:
            print("Enter valid seat number")
        elif self.__booked_seat + seat <= self.__total_seat:
            self.__booked_seat += seat
            print(seat,"Seat booked successfully")
        else:
            print("Sorry! There is no available seat")

    def cancel_seat(self):
        seat = int(input("Enter seat you want to cancel :"))
        if seat <= 0:
            print("Please enter valid seat number")
        elif seat <= self.__booked_seat:
            self.__booked_seat -= seat
            print(seat,"Seat cancelled successfully")

        else:
            print("Invalid cancellation! No seats booked")

    def display(self):
        available_seat = self.__total_seat - self.__booked_seat
        print(f"--------------------Train Details--------------------")
        print(f"Train Number : {self.__train_number}\nTotal Seat : {self.__total_seat}\nBooked Seat : {self.__booked_seat}\nAvailable Seat : {available_seat}")

t1 = Train(1234,20)
t1.reserve_seat()
t1.reserve_seat()
t1.cancel_seat()
t1.display()

