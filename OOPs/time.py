class time:
    def __init__(self,hours,minutes,seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def add(self,a,b):
        temp = time(0,0,0)
        temp.__hours = self.__hours + a.__hours + b.__hours
        temp.__minutes = self.__minutes + a.__minutes + b.__minutes
        temp.__seconds = self.__seconds + a.__seconds + b.__seconds
        if temp.__seconds >= 60:
            temp.__minutes += 1
            temp.__seconds -= 60
        if temp.__minutes >= 60:
            temp.__hours += 1
            temp.__minutes -= 60
        return temp
    def display(self):
        print(f"{self.__hours} hours : {self.__minutes} minutes : {self.__seconds} seconds")

t1 = time(2,50,50)
t2 = time(1,15,40)
t3 = time(0,0,0)
t1.display()
t2.display()
t3.display()

t4 = t3.add(t1,t2)
t4.display()

