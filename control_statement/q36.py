n = int(input("Enter number :"))
a = 0
while(n>0):
    rem = n%10
    a =a*10+rem
    n = n//10
print(f"Reverse is :{a}")