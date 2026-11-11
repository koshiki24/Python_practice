'''13. Exam Portal
Problem

Create exam management system.

Requirements

Each exam object:

exam name
total marks
passing marks
Functionalities
Check pass/fail
Calculate grade
Maintain total exams conducted'''

class Exam:
    total_exams = 0
    def __init__(self,exam_name,total_marks,passing_marks,obtained_marks):
        self.__exam_name = exam_name
        self.__total_marks = total_marks
        self.__passing_marks = passing_marks
        self.__obtained_marks = obtained_marks

        Exam.total_exams +=1

    def check(self):
        if self.__obtained_marks >= self.__passing_marks:
            print("Result:Pass")
        else:
            print("Result:Fail")

    def grade(self):
        percentage = (self.__obtained_marks/self.__total_marks)*100
        if percentage > 90:
            print("Grade A+")
        elif percentage >=75 and percentage<=90:
            print("Grade A")
        elif percentage >=60 and percentage<=74:
            print("Grade B")
        elif percentage>=33 and percentage<60:
            print("Grade C")
        else:
            print("Grade D or Fail")

    def display(self):
        print(f"Exam Name : {self.__exam_name}")
        print(f"Total Marks : {self.__total_marks}")
        print(f"Passing marks : {self.__passing_marks}")
        print(f"Obtained Marks : {self.__obtained_marks}")

    @classmethod
    def total_exam(cls):
        print(f"Total Exam Conducted : {cls.total_exams}")

e1 = Exam("Python",100,33,95)
e2 = Exam("Physics",100,33,90)
e3 = Exam("Maths",100,33,98)

e1.display()
e1.check()
e1.grade()
print("\n")

e2.display()
e2.check()
e2.grade()
print("\n")

e3.display()
e3.check()
e3.grade()

Exam.total_exam()

        
