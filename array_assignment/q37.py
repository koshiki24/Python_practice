print("Write a python program to implement insertion sort algorithm")
arr = [2, 5, 1, 10, 8, 60, 90, 100]
for i in range(1,len(arr)):
    j = i

    while j > 0 and arr[j] < arr[j-1]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j -= 1
print(arr)
