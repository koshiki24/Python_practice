a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
for i in range(a,b+1):
    a = 1
    while(a<=10):
        print(f"{i}*{a}={i*a}",end="")
        a+=1
    print()
    