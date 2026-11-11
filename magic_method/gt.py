class Greater:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __gt__(self,sd):
        if self.__km > sd.__km and self.__meter > sd.__meter:
            return True
        else:
            return False

g1 = Greater(10,5)
g2 = Greater(5,4)
print(g1 > g2)