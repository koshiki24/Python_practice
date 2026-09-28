n = int(input("Enter number"))
last = n%10
temp = n
for i in range(n):
 if temp < 10:
    first = temp
    break
  temp = temp//10

 sum = first+last
 print(f"Sum is : {sum}")
