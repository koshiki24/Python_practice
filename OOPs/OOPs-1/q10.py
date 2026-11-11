'''Write a Java program to create a class called "Student" with a name, grade, and courses attributes, and methods to add and remove courses.
'''

class Student:
    def __init__(self,name,grade,courses):
        self.__name = name
        self.__grade = grade
        self.__courses = courses
    

    def add_courses(self):
        course = input("Enter course :")
        self.__courses.append(course)
        print("Course added successfully")

    def remove_courses(self):
        course = input("Enter courses to remove :")
        self.__courses.remove(course)
        print("Course removed Successfully")

    def display(self):
        print(f"Name : {self.__name}, Grade : {self.__grade}, Course : {self.__courses}")
s1 = Student("Koshiki","A",["Maths","Science"])
s1.display()
s1.remove_courses()
s1.display()

