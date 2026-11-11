print("Write a Java program to find the largest and smallest element of an array.")
arr = [8,2,20]
largest = arr[0]
smallest = arr[0]
for i in range(len(arr)):
    if largest < arr[i]:
        largest = arr[i]
    if smallest > arr[i]:
        smallest = arr[i]
print(f"Largest is : {largest}")
print(f"Smallest is : {smallest}")