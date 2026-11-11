print("Write a java program to implement selection sort algoritm")
arr = [2, 5, 1, 10, 8, 60, 90, 100]
for i in range(len(arr)-1):
    smallest = i
    for j in range(i+1,len(arr)):
        if arr[smallest] > arr[j]:
            smallest = j
    arr[i],arr[smallest] = arr[smallest],arr[i]
print(arr)
