# '''8. Employee Attendance and Salary Calculator
# Intermediate
# Concepts: Conditions, loops, functions, dictionaries
# Requirements
# •	Enter employee details and days present.
# •	Calculate attendance percentage.
# •	Calculate salary based on days worked.
# •	Apply a bonus or deduction according to attendance rules.
# •	Generate an employee summary.
# '''

def emp_details():
    emp = {}

    emp["name"] = input("Enter Employee Name: ")
    emp["id"] = input("Enter employee id: ")
    emp["salary"] = float(input("Enter monthly salary: "))
    emp["working_day"] = int(input("Enter total working days: "))
    emp["present_day"] = int(input("Enter days present: "))

    return emp


def calculate_salary(emp):
    attendance = (emp["present_day"] / emp["working_day"]) * 100
    daily_salary = emp["salary"] / emp["working_day"]
    salary = daily_salary * emp["present_day"]

    bonus = 0
    deduction = 0

    if attendance > 95:
        bonus = 1000
    elif attendance >= 75 and attendance <= 95:
        bonus = 500
    else:
        deduction = 500

    final_salary = salary + bonus - deduction

    print("\n-----------------Employee Summary------------------")
    print(f"Employee's Name: {emp['name']}")
    print(f"Employee's ID: {emp['id']}")
    print(f"Monthly Salary: {emp['salary']}")
    print(f"Days Present: {emp['present_day']}")
    print(f"Working Days: {emp['working_day']}")
    print(f"Attendance Percentage: {attendance}%")
    print(f"Earned Salary: {salary}")
    print(f"Bonus: {bonus}")
    print(f"Deduction: {deduction}")
    print(f"Final Salary: {salary}")


employee = emp_details()

if (employee["working_day"] > 0
    and employee["salary"] >= 0
    and employee["present_day"] >= 0
    and employee["present_day"] <= employee["working_day"]):
    calculate_salary(employee)
else:
    print("Invalid attendance details!")
