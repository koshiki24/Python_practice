a = int(input("Enter number :"))
b = int(input("Enter number :"))
if a<b:
    small = a
else:
    small = b
for i in range(small,a*b+1):
     if i%a == 0 and i%b == 0:
        print(i)
        break
    