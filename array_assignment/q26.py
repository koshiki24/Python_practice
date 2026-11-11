print("Write a Java program to reverse the element of an integer 1-D array. ")
arr = [8,3,1,2]
print(f"Before reversing : {arr}")
left = 0
right = len(arr)-1
while (left < right):
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(f"After reversing : {arr}")
