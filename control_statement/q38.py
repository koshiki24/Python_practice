'''n = int(input("Enter number: "))

temp = n
sum = 0

while n > 0:
    r = n % 10
    sum = sum + r ** 3
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")'''

n = int(input("Enter number :"))
temp = n
digit=0
sum = 0
while(n!=0):
    digit+=1
    n//=10
while(n>0):
    r = n%10
    sum = sum+r**digit
    temp//=10
if n == sum:
    print("Armstrong")
else:
    print("Not armstrong")