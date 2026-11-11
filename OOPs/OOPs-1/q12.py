''' Write a Java program to create a class called "Airplane" with a flight number, destination, and departure time attributes, and methods to check flight status and delay.
'''

class Airplane:

    def __init__(self,flight_number,destination,departure_time):
        self.__flight_number = flight_number
        self.__destination = destination
        self.__departure_time = departure_time
        self.__status = "Delay"
        self.__delay = 0

    def check_status(self):
        print(f"Flight Number : {self.__flight_number}")
        print(f"Destination : {self.__destination}")
        print(f"Departure Time : {self.__departure_time}")
        print(f"Status : {self.__status}")

    def check_delay(self):
        if self.__delay > 0:
            print(f"Flight is delayed by : {self.__delay} minutes")
        else:
            print("Flight is on time")

    def update_status(self,status):
        self.__status = status

    def update_delay(self,delay):
        self.__delay = delay

a1 = Airplane(123,"Dubai",1200)
a1.check_status()
a1.update_status("On Time")
a1.check_status()