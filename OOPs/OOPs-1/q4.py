'''Write a Java program to create a class called "Circle" with a radius attribute. You can access and modify this attribute. Calculate the area and circumference of the circle.
'''

class Circle:
    def __init__(self,rad):
        self.__rad = rad
    def area(self):
        return 3.14*self.__rad*self.__rad
    def circumference(self):
        return 2*3.14*self.__rad
    def set_radius(self,radius):
        self.__rad = radius
    def get_radius(self):
        return self.__rad
    def display(self):
        print(f"Area of circle is : {self.area()}")
        print(f"Circumference of circle is : {self.circumference()}")
c1 = Circle(8)
c1.display()
c1.set_radius(6)
print(c1.get_radius())
c1.display()