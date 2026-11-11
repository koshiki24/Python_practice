class Add:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __add__(self,sd):
        temp = Add(0,0)
        temp.__km = self.__km + sd.__km
        temp.__meter = self.__meter + sd.__meter

        if temp.__meter >= 1000:
            temp.__km+=1
            temp.__meter-=1000
        return temp

    def __str__(self):
        return f"{self.__km} km and {self.__meter} meter"

a1 = Add(10,500)
a2 = Add(5,500)
a3 = a1+a2
print(a3)