class Multiplication:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __mul__(self,sd):
        temp = Multiplication(0,0)
        temp.__km = self.__km * sd.__km
        temp.__meter = self.__meter * sd.__meter

        if temp.__meter >= 1000:
            temp.__km+=1
            temp.__meter-=1000
        return temp

    def __str__(self):
        return f"{self.__km} km and {self.__meter} meter"

d1 = Multiplication(5,10)
d2 = Multiplication(5,110)
d3 = d1 * d2
print(f"Total distance is : {d3}")