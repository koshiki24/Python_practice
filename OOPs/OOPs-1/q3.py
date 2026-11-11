'''Write a Java program to create a class called "Rectangle" with width and height attributes. Calculate the area and perimeter of the rectangle.'''

class Rectangle:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
    def area(self):
        temp = self.__width * self.__height
        return temp
    def perimeter(self):
        temp = 2*(self.__width + self.__height)
        return temp
    def display(self):
        print(f"Area of rectangle is : {self.area()}")
        print(f"Perimeter of rectangle is : {self.perimeter()}")
r1 = Rectangle(2,3)
r1.display()