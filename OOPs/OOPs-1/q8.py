'''Write a Java program to create class called "TrafficLight" with attributes for color and duration, and methods to change the color and check for red or green.
'''

class TrafficLight:
    def __init__(self,color,duration):
        self.__color = color
        self.__duration = duration

    def change_color(self,new_color):
        self.__color = new_color
        print("Traffic light or color changed successfully!!")

    def is_red(self):
        if self.__color == "red":
            return True
        else:
            return False

    def is_green(self):
        if self.__color == "green":
            return True
        else:
            return False

    def display(self):
        print(f"Color : {self.__color}")
        print(f"Duration : {self.__duration} seconds")

t1 = TrafficLight("red",30)
t2 = TrafficLight("green",15)
t1.display()

print("Is Red", t1.is_red())
print("Is Green",t2.is_green())