print("Sub array with given sum")

arr = [5,2,7,3,10]
sum = 0
target = 12
left = 0
for right in range(len(arr)):
    sum = sum + arr[right]
    while sum > target or left > right:
        sum=sum-arr[left]
        left+=1

    if sum == target:
        print(f"{left+1},{right+1}")
else:
    print("No sub array found")