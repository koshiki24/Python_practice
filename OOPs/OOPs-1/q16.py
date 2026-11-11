'''Write a Java program to create a class called "Shape" with abstract methods for calculating area and perimeter, and subclasses for "Rectangle", "Circle", and "Triangle".
'''

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        area = self.__length * self.__breadth
        return area

    def perimeter(self):
        perimeter = 2 * (self.__length + self.__breadth)
        return perimeter

class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius

    def area(self):
        area = 3.14 * self.__radius**2
        return area

    def perimeter(self):
        perimeter = 2 * 3.14 * self.__radius
        return perimeter

class Triangle(Shape):
    def __init__(self,base,height,side1,side2):
        self.__base = base
        self.__height = height
        self.__side1 = side1
        self.__side2 = side2

    def area(self):
        area = 0.5 * self.__base * self.__height
        return area

    def perimeter(self):
        perimeter = self.__base + self.__side1 + self.__side2
        return perimeter

r = Rectangle(2,2)
print(f"Rectangle area : {r.area()}")
print(f"Rectangle perimeter : {r.perimeter()}")

c = Circle(3)
print(f"Circle area : {c.area()}")
print(f"Circle perimeter : {c.perimeter()}")

t = Triangle(2,3,4,4)
print(f"Triangle area : {t.area()}")
print(f"Triangle perimeter : {t.perimeter()}")




    