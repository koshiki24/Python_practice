'''18. School Classroom System
Problem

Create classroom system.

Requirements

Classroom should:

maintain student objects
maintain class teacher
Functionalities
Add student
Remove student
Display class strength
Concepts Practiced
object aggregation
collections of objects'''

class Student:
    def __init__(self,roll_no,name):
        self.__roll_no = roll_no
        self.__name = name
    def get_roll_no(self):
        return self.__roll_no
    def get_name(self):
        return self.__name

class Classroom:
    def __init__(self,class_name,class_teacher):
        self.__class_name = class_name
        self.__class_teacher = class_teacher
        self.__students = []
    def add_student(self,student):
        self.__students.append(student)
        print(student.get_name(),"added successfully")
    def remove_student(self,roll_no):
        for student in self.__students:
            if student.get_roll_no() == roll_no:
                self.__students.remove(student)
                print(student.get_name(),"removed successfully!")
                return
            print("student not found")

    def display_student(self):
        print("------------Student Details----------")
        print(f"Class : {self.__class_name}\nClass Teacher : {self.__class_teacher}")

        if len(self.__students) == 0:
            print("No student in this classroom")
        else:
            for student in self.__students:
                print(f"Roll No. : {student.get_roll_no()}\nName : {student.get_name()}")
    def display_class_strength(self):
        print("\nClass Strength:", len(self.__students))

s1 = Student(1, "Koshiki")
s2 = Student(2, "Shriya")
s3 = Student(3, "Kashish")
s4 = Student(4, "Abhisha")

c1 = Classroom("12th CSE", "Mr. Sharma")

c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
c1.add_student(s4)

c1.display_student()

c1.display_class_strength()

c1.remove_student(2)

c1.display_student()
c1.display_class_strength()


