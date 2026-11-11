class modulus:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __mod__(self,sd):
        temp = modulus(0,0)
        temp.__km = self.__km % sd.__km
        temp.__meter = self.__meter % sd.__meter
        return temp

    def __str__(self):
        return f"{self.__km} km and {self.__meter} meter"

m1 = modulus(5,10)
m2 = modulus(2,5)
m3 = m1 % m2
print(m3)

        