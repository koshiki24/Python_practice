n = int(input("Enter number :"))
temp = n
sum = 0
i = 1
while(i<n):
    if n%i==0:
        sum = sum+i
    i+=1
if sum == temp:
        print("Number is perfect")
else:
        print("Number is not perfect")