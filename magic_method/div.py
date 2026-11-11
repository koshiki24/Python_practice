class Division:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __truediv__(self,sd):
        temp = Division(0,0)
        temp.__km = self.__km / sd.__km
        temp.__meter = self.__meter / sd.__meter
        if sd.__km <= 0 or sd.__meter <= 0:
            print("It cant be divide because value is 0")

        return temp

    def __str__(self):
        return f"{self.__km} km and {self.__meter} meter"

d1 = Division(10,15)
d2 = Division(2,3)
d3 = d1 / d2
print(f"Division is : {d3}")