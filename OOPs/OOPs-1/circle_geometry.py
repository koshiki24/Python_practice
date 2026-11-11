'''Circle Geometry
Create a class Circle with field radius.
Use a setter to assign radius. Add methods to compute area and circumference.'''

import math

class Circle:

    def __init__(self):
        self.__radius = 0.0

    # Setter method
    def set_radius(self, radius):
        self.__radius = radius

    # Calculate area
    def calculate_area(self):
        return math.pi * self.__radius * self.__radius

    # Calculate circumference
    def calculate_circumference(self):
        return 2 * math.pi * self.__radius

    # Display details
    def display(self):
        print("Radius :", self.__radius)
        print("Area :", self.calculate_area())
        print("Circumference :", self.calculate_circumference())


c1 = Circle()

c1.set_radius(5)

c1.display()