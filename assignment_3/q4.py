english = int(input("Enter marks : "))
hindi = int(input("Enter marks : "))
science = int(input("Enter marks : "))
social = int(input("Enter marks : "))
maths = int(input("Enter marks : "))
total = english + hindi + science + social + maths
percentage = (total/500)*100
if percentage > 80:
 print(f"A")
elif percentage >60 and percentage <= 80:
 print(f"B")
elif percentage > 50 and percentage <= 60:
 print(f"C")
elif percentage >45 and percentage <= 50:
 print(f"D")
elif percentage >25 and percentage <= 45:
 print(f"E")
else:
 print(f"F")

