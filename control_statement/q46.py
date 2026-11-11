'''n = int(input("Enter number"))
last = n%10
temp = n
for i in range(n):
 if temp < 10:
    first = temp
    break
  temp = temp//10

 sum = first+last
 print(f"Sum is : {sum}")'''

n = int(input("Enter number :"))
temp = n
digit = 0
last=n%10
while(n!=0):
    digit+=1
    n//=10
first = temp//(10**(digit-1))
sum = first+last
print(sum)
