print("Write a java program to implement bubble sort algorithm")
arr = [2, 5, 1, 10, 8, 60, 90, 100]
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)