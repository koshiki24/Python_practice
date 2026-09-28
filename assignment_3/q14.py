percentage = float(input("Enter the percentage here : "))
if percentage>=90:
    print(f"Grade is A")
elif percentage>80 and percentage<=90:
    print(f"Grade is B")    
elif percentage>=60 and percentage<=80:
    print(f"Grade is C")
elif percentage<60:
    print(f"Grade is D")
else:
    print("Invalid number ")