print("Write a python program to implement linear search")
arr = [1, 2, 3, 4, 9, 10, 20]
n = int(input("Enter element to be found :"))
for i in range(len(arr)):
    if arr[i] == n:
        print(f"Element found at index {i}")
        break
else:
    print("Element not found")