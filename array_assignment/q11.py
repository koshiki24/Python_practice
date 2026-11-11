print("Write a program to cyclically rotate array by one")
arr = [10,5,2,3,15]
left = 0
right = len(arr)-1
a = arr[right]
for i in range(len(arr)-1,-1,-1):
    arr[i] = arr[i-1]
arr[0] = a
print(arr)