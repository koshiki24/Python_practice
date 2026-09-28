a = int(input("Enter the age of first person :"))
b = int(input("Enter the age of second person :"))
c = int(input("Enter the age of third person :"))
if a > b and a > c:
 oldest = 'a'
elif b > a and b > c:
 oldest = 'b'
else:
 oldest = 'c' 
if a < b and a < c:
 youngest = 'a'
elif b < a and b < c:
 youngest = 'b'
else:
 youngest = 'c'
print(f"Oldest is {oldest}")
print(f"Youngest is {youngest}")