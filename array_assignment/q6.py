print("Find occurance of an integer number in array.")
n = int(input("Enter number :"))
arr = [10,5,5,40,12,18]
count = 0
for i in range(len(arr)):
    if arr[i] == n:
        count+=1
print(f"Occurance of a integer is : {count}")
