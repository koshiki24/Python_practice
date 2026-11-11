class Less:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter

    def __lt__(self,sd):
        if self.__km < sd.__km and self.__meter < sd.__meter:
            return True
        else:
            return False

l1 = Less(1,2)
l2 = Less(8,6)
print(l1 < l2)