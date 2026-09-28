n = int(input("Enter number :"))
count_even = 0
count_odd = 0
i = 1
while(i<=n):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
    i+=1
print(f"Even number is : {count_even}")
print(f"Odd number is : {count_odd}")
