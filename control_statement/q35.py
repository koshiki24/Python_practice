n = int(input("Enter digits :"))
count = 0
i = 1
while(n>0):
    n = n//10
    count+=1
print(count)