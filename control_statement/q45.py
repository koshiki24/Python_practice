n = int(input("Enter number :"))
sum = 0
for i in range(n):
    a=n%10
    sum = sum+a
    n = n //10
print(f"Sum is : {sum}")