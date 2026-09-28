a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
for i in range(a,b+1):
    c=1
    while(c<=i):
        if i%c==0:
          print(c,end=" ")
        c+=1
    print()