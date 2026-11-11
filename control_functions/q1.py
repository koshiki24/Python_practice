print('''1. Smart Calculator
Beginner
Concepts: if-elif-else, while, functions
Requirements
•	Display a menu for addition, subtraction, multiplication, division, and modulus.
•	Take two numbers from the user.
•	Use separate functions for each operation.
•	Handle division by zero.
•	Repeat until the user selects Exit.
Bonus: Add power and floor division operations.
''')
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "It is not possible"
    else:
        return a/b
def mod(a,b):
    if b == 0:
        return "Cannot perform modulus by zero"
    else:
        return a%b
def power(a,b):
    return a**b
def floor_div(a,b):
    if b == 0:
        return "Floor division is not possible"
    else:
        return a//b

while True:
    print("1. For Addition")
    print("2. For Subtraction") 
    print("3. For Multiplication") 
    print("4. For Division")
    print("5. For Modulus")
    print("6. For Power")
    print("7. For Floor Division")
    print("8. Exit")

    choice = int(input("Enter choice :"))
    if choice == 8:
        print("Calculator Closed")
        break
    elif choice >=1 and choice <=7:
        a = int(input("Enter first value :"))
        b = int(input("Enter second value :"))
        if choice == 1:
            print(f"Addition is : {add(a,b)}")
        elif choice == 2:
            print(f"Subtraction is : {sub(a,b)}")
        elif choice == 3:
            print(f"Multiplication is : {mul(a,b)}")
        elif choice == 4:
            print(f"Division is : {div(a,b)}")
        elif choice == 5:
            print(f"Modulus is : {mod(a,b)}")
        elif choice == 6:
            print(f"Power is : {pow(a,b)}")
        elif choice == 7:
            print(f"Floor division is : {floor_div(a,b)}")
    else:
        print("Invalid Choice")