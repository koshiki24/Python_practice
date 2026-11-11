print("Find the first repeating element in array of integers")
arr = [1,2,7,8,8,9,5,5]
for i in range(len(arr)-1):
    count = 0
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            count+=1
    if count == 1:
        print(arr[i])
        break
else:
    print("There is no repeating element")
    
