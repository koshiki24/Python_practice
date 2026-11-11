print("Find the kth largest and kth smallest element in array.")

arr = [10,5,5,3,8,9]
k = int(input("Enter index for smallest and largest :"))

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(f"Sorted array is {arr}")
smallest = arr[k-1]
largest = arr[len(arr)-k]
print(f"Smallest is {smallest}")
print(f"Largest is {largest}")
