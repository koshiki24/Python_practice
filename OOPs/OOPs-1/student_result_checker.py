'''Student Result Checker
Create a class Student with fields: name, mathMarks, scienceMarks.
Use setters to assign values. Add a method getAverage().'''

class Student:

    def __init__(self):
        self.__name = ""
        self.__mathMarks = 0
        self.__scienceMarks = 0

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_math_marks(self, marks):
        self.__mathMarks = marks

    def set_science_marks(self, marks):
        self.__scienceMarks = marks

    # Calculate average
    def getAverage(self):
        average = (self.__mathMarks + self.__scienceMarks) / 2
        return average

    # Display student details
    def display(self):
        print("Student Name :", self.__name)
        print("Math Marks :", self.__mathMarks)
        print("Science Marks :", self.__scienceMarks)
        print("Average Marks :", self.getAverage())


s1 = Student()

s1.set_name("Shriya")
s1.set_math_marks(85)
s1.set_science_marks(90)

s1.display()