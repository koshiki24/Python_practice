maths = float(input("enter the marks of maths:"))
science = float(input("enter the marks of science:"))
hindi = float(input("enter the marks of hindi:"))
english = float(input("enter the marks of english:"))
social_science = float(input("enter the marks of social science:"))


total = maths + science + hindi + english + social_science
percentage = total / 5

if percentage > 90 :
    print(f"Grade A and marks is : {percentage}")
elif percentage >= 80 and percentage <=90:
    print(f"Grade B and marks is : {percentage}")
elif percentage >=70 and percentage <=79:
    print(f"Grade C and marks is : {percentage}")
elif percentage >= 60 and percentage <=69:
    print(f"Grade D and marks is : {percentage}")
elif percentage >= 40 and percentage <=59:
    print(f"Grade E and marks is : {percentage}")
elif percentage > 0 and percentage <=39:
    print(f"Grade F and marks is : {percentage}")

    
else  :
    print("Invalid number ")