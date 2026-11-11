print("P is one-dimensional array of integers.Write aJava program search for a data VAL from P. If VAL is present in the array then “element found ”otherwise“elementnot found” should be displayed.")
arr = [1,9,3,10,4,20,2]
n = int(input("Enter element to be found :"))
for i in range(len(arr)):
    if arr[i] == n:
        print(f"Element found at index {i}")
        break
else:
    print("Element not found")
