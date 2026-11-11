print("Find minimum and maximum element in array")
arr = [10,5,15,25,20,20]
minimum = arr[0]
maximum = arr[0]
for i in range(len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
    elif arr[i] > maximum:
        maximum = arr[i]
print(f"Minimum is : {minimum}")
print(f"Maximum is : {maximum}")