a = int(input("Enter number :"))
b = int(input("Enter number :"))
if a < b:
    small = a
else:
    small = b
for i in range(small,0,-1):
    if a%i == 0 and b%i == 0:
        print(f"HCF is : {i}")
        break
