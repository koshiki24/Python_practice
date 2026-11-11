print('''2. Student Result Management System
Beginner
Concepts: Conditions, loops, functions
Requirements
•	Input marks for five subjects.
•	Calculate total, percentage, and grade.
•	Check whether the student passed or failed.
•	Validate that each mark is between 0 and 100.
•	Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
Bonus: Accept results for multiple students and calculate the class average.
''')
def calculate_total(a,b,c,d,e):
    total = a+b+c+d+e
    return total

def calculate_percentage(a,b,c,d,e):
    total = a+b+c+d+e
    percentage = total/5
    return percentage
def marks(a,b,c,d,e):
    return a,b,c,d,e
def calculate_grade(a,b,c,d,e):
    total = a+b+c+d+e
    percentage = total/5
    if percentage >=75 and percentage<=100:
        return "Grade A"
    elif percentage >=60 and percentage < 75:
        return "Grade B"
    elif percentage >= 40 and percentage < 60:
        return "Grade C"
    else:
        return "Grade D"
    
student = []
while True:
    print("1.Enter marks for students :")
    print("2.Calculate the class average :")
    print("3.Calculate Total :")
    print("4.Calculate Percentage :")
    print("5.Calculate Grade :")
    print("6.Pass or Fail :")
    print("7.Exit")

    choice = int(input("Enter choice :"))
    if choice == 7:
        print("Closed")
        break
    elif choice == 1:
        students = int(input("enter number of students you want add :"))
        for i in range(students):
            print(f"Enter marks for {i+1}")
            a = int(input("Enter marks for first subject :"))
            b = int(input("Enter marks for second subject :"))
            c = int(input("Enter marks for third subject :"))
            d = int(input("Enter marks for fourth subject :"))
            e = int(input("Enter marks for fifth subject :"))
            if a<0 or a>100 or b<0 or b>100 or c<0 or c>100 or d<0 or d>100 or e<0 or e>100:
                print("Invalid Marks! Enter marks between 1 to 100")
            else:
                student.append([a,b,c,d,e])
                print(f"Student {len(student)}  added successfully")
    elif choice == 2:
        if len(student) > 0:
            total_percentage = 0

            for i in range(len(student)):
                a, b, c, d, e = student[i]
                total_percentage += calculate_percentage(a, b, c, d, e)

            average = total_percentage / len(student)
            print("Class average:", average, "%")
        else:
            print("No student records found!")
        
    elif choice == 3:
        for i in range(len(student)):
            a,b,c,d,e = student[i]
            print(f"Student {i+1} total : {calculate_total(a,b,c,d,e)}")
    elif choice == 4:
        for i in range(len(student)):
            a,b,c,d,e = student[i]
            print(f"Student {i+1} Percentage : {calculate_percentage(a,b,c,d,e)}")
    elif choice == 5:
        for i in range(len(student)):
            a,b,c,d,e = student[i]
            print(f"Student {i+1} grade : {calculate_grade(a,b,c,d,e)}")
    elif choice == 6:
        for i in range(len(student)):
            a,b,c,d,e = student[i]
            if  a > 33 and b > 33 and c > 33 and d > 33 and e > 33:
                print(f"Student {i+1} is Pass")
            else:
                print(f"Student {i+1} is Fail")
else:
    print("Invalid Choice")


