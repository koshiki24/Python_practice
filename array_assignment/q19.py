print("Find largest sum contiguous sub array")

arr = [1, -5, 10, -3]
largest = arr[0]

for i in range(len(arr)):
    sum = 0

    for j in range(i,len(arr)):
        sum = sum + arr[j]

        if sum > largest:
            largest = sum

print(largest)