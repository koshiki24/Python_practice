print("Find the first non repeating element")
arr = [1,1,1,1,5]
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count+=1
    if count == 1:
        print(arr[i])
        break
else:
    print("All elements are repeting")