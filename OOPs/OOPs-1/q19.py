'''Write a Java program to create a class with methods to search for flights and hotels, and to book and cancel reservations.'''

class Reserve:
    def __init__(self):
        self.flights = ["Indigo","Air India","Vistara","Qatar Airways"]
        self.hotels = ["Radisson","Taj","ITC","Marriott"]
        self.reservation = []

    def search_flight(self):
        flight = input("Enter flight name you want to search :")
        if flight in self.flights:
            print(f"Yes flight name {flight} is available")
        else:
            print("No flight available")

    def search_hotel(self):
        hotel = input("Enter hotel name you want to search :")
        if hotel in self.hotels:
            print(f"Yes {hotel} is available")
        else:
            print("Hotel not found!")

    def book(self):
        name = input("Enter reservation name :")
        self.reservation.append(name)
        print("Reservation booked successfully")

    def cancel(self):
        name = input("Enter reservation name you want to cancel :")
        if name in self.reservation:
            self.reservation.remove(name)
            print("Reservation cancelled successfully!")
        else:
            print("Reservation not found")

r = Reserve()

while True:
    print("\n1. Search Flight")
    print("2. Search Hotel")
    print("3. Book Reservation")
    print("4. Cancel Reservation")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r.search_flight()
    elif choice == 2:
        r.search_hotel()
    elif choice == 3:
        r.book()
    elif choice == 4:
        r.cancel()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

