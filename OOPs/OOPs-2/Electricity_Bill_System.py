'''17. Electricity Bill System
Problem

Generate electricity bill.

Requirements

Consumer should contain:

consumer id
units consumed
Functionalities
Calculate bill
Add surcharge using static method
Display bill summary'''

class Consumer:
    def __init__(self,consumer_id,units_consumed):
        self.__consumer_id = consumer_id
        self.__units_consumed = units_consumed
    def calculate_bill(self):
        units = self.__units_consumed
        if units <=100:
            bill = units * 3
        elif units <=200:
            bill = (100*3)+(units-100)*5
        elif units <=300:
            bill = (100*3)+(100*5)+(units-200)*7
        else:
            bill = (100*3)+(100*5)+(100*7)+(units-300)*10
        return bill

    @staticmethod
    def add_surcharge(bill):
        return bill * 5 / 100

    def display_bill(self):
        print("--------------------Electricity Bill--------------------")
        bill = self.calculate_bill()
        surcharge = Consumer.add_surcharge(bill)

        print(f"Consumer Id : {self.__consumer_id}\nUnits Consumed : {self.__units_consumed}\nElectricity Bill : {bill}\nSurcharge : {surcharge}\nFinal Bill Amount : {bill + surcharge}")
        print("------------------------------")
c1 = Consumer(12345,99)
c2 = Consumer(123456,199)
c1.calculate_bill()
c1.add_surcharge(c1.calculate_bill())
c1.display_bill()
c2.calculate_bill()
c2.add_surcharge(c2.calculate_bill())
c2.display_bill()



