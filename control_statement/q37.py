n = int(input("Enter number :"))
original = n
a = 0
while(n>0):
    rem = n%10
    a =a*10+rem
    n = n//10
print(f"Reverse is :{a}")
if a == original:
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")