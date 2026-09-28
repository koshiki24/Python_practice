class_held = int(input("Enter number of class held :"))
class_attended = int(input("Enter number of class attended :"))
percentage = (class_attended/class_held)*100
print(f"Number of class attended {percentage}")
if percentage >= 75:
 print(f"Student is allowed to sit in exam")
else: 
 print(f"Student are not able to sit in exam")
