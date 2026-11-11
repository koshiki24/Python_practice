print("Longest consecutive sequence")
arr = [1,5,7,20,21,22]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

count = 1
longest = 1
for i in range(len(arr)-1):
    if arr[i+1] == arr[i]+1:
        count+=1
    elif arr[i+1] != arr[i]:
        count = 1
    if count > longest:
        longest = count
print(longest)
