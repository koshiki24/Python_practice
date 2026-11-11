'''4. Student Grade System
Problem

Create a student result management system.

Requirements

Each student should have:

roll number
name
marks in 3 subjects
Functionalities
Calculate total marks
Calculate percentage
Assign grade:
A → 90+
B → 75+
C → 50+
Fail otherwise
Track total students
Concepts Practiced
instance methods
conditional logic in classes
object-based calculations'''

class Student:
    student_list = {}

    def __init__(self,roll_number):
        self.__roll_number = roll_number
        self.__name = input("Enter student name :")

        marks = []
        for i in range(3):
            mark = float(input(f"Enter marks for {i+1} subject :"))
            marks.append(mark)
        Student.student_list[self.__roll_number] = {
            "name": self.__name,
            "marks": marks
        }
        return

    def calculate_total(self):
        total = 0
        for mark in Student.student_list[self.__roll_number]["marks"]:
            total += mark
        return total

    def calculate_per(self):
        percentage = self.calculate_total() * (100/300)
        return percentage

    def grade(self):
        if self.calculate_per() >= 90:
            return "A"
        elif self.calculate_per() >= 75:
            return "B"
        elif self.calculate_per() >= 50:
            return "C"
        else:
            return "Fail"

    @classmethod
    def display_student(cls):
        for roll_no, student in cls.student_objects.items():
            print("\n------------------------")
            print("Student Name:", cls.student_list[roll_no]["name"])
            print("Roll Number:", roll_no)
            print("Marks:", cls.student_list[roll_no]["marks"])
            print("Total Marks:", student.calculate_total())
            print("Percentage:", student.calculate_per())
            print("Grade:", student.grade())    
    
    def total_student(self):
        return len(Student.student_list)

s1 = Student(101)
s1 = Student(102)

s1.display_student()
print(f"Total Students : {s1.total_student()}")





        
