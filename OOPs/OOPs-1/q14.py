'''Write a Java program to create a class called "School" with attributes for students, teachers, and classes, and methods to add and remove students and teachers, and to create classes.
'''
class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classes = []

    def add_student(self):
        st = input("Enter student name :")
        self.students.append(st)

    def add_teacher(self):
        t = input("Enter teacher name :")
        self.teachers.append(t)

    def remove_student(self):
        st = input("Enter student you want to remove : ")
        for i in range(len(self.students)):
            if self.students[i] == st:
                self.students.pop(i)
            else:
                print("Student not found!!")

    def remove_teacher(self):
        t = input("Enter teacher you want to remove :")
        for i in range(len(self.teachers)):
            if self.teachers[i] == t:
                self.teachers.pop(i)
            else:
                print("Teacher not found!!")

    def create_class(self):
        cl = input("Enter class name : ")
        self.classes.append(cl)


    def display(self):
        print(f"Students are :{self.students}")
        print(f"Teachers are : {self.teachers}")
        print(f"Classes are : {self.classes}")

    

s1 = School()
s1.add_student()
s1.add_student()
s1.create_class()
s1.add_teacher()
s1.add_student()

s1.display()

# s1.add_teacher()
# s1.add_teacher()
# s1.add_teacher()

s1.display()

s1.remove_teacher()

s1.remove_student()


s1.display()
