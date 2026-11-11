print("Find it there is any subarray with sum equals to zero")
arr = [4, 2, -3, 1, 6]
flag = False
for i in range(len(arr)-1):
    sum = 0

    for j in range(i,len(arr)):
        sum = sum+arr[j]
        if sum == 0:
            flag = True
            print(f"{i},{j}")
            break
if flag == False:
    print("No sub array found")