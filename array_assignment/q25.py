print("Write a Java program to swap first and last element of an integer 1-d array.")
arr = [8,3,1,2]
print(f"Before Swapping : {arr}")
right = len(arr)-1
temp = arr[0]
arr[0] = arr[right]
arr[right] = temp
print(f"After Swapping : {arr}")
