class Distance:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __sub__(self,sd):
        temp = Distance(0,0)
        temp.__km = self.__km - sd.__km
        temp.__meter = self.__meter - sd.__meter
        return temp

    def __str__(self):
        return f"{self.__km} km {self.__meter} meter"

d1 = Distance(10,900)
d2 = Distance(5,500)
d3 = d1 - d2
print(d3)