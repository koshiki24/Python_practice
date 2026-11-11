print("Write a python program to impelment binary search algorithm")
n = int(input("Enter element to be found : "))
arr = [1, 2, 3, 4, 9, 10, 20]
left = 0
right = len(arr)-1
while(left<=right):
    mid = (left+right)//2
    if arr[mid] == n:
        print(f"Element found at index {mid}")
        break
    elif arr[mid] < n:
        left = mid+1
    elif arr[mid] > n:
        right = mid-1
else:
    print("Element not found")

