'''Rectangle Area Calculator
Create a class Rectangle with fields: length, width.
Use setters to assign values. Add a method to calculate area'''

class Rectangle:

    def __init__(self):
        self.__length = 0.0
        self.__width = 0.0

    # Setter methods
    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    # Calculate area
    def calculate_area(self):
        return self.__length * self.__width

    # Display details
    def display(self):
        print("Length :", self.__length)
        print("Width :", self.__width)
        print("Area :", self.calculate_area())


r1 = Rectangle()

r1.set_length(10)
r1.set_width(5)

r1.display()