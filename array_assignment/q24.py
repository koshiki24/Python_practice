print("Write a Python program to find the sum and average of one dimensional integer array")
arr = [8,3,1,2]
sum = 0
for i in range(len(arr)):
    sum = sum+arr[i]
print(f"Sum is : {sum}")
average = sum/len(arr)
print(f"Average is : {average}")