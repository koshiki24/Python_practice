print("Java program to find nearest lesser and greater element in array")
arr=[8,3,1,2]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

k = int(input("Enter element : "))

index = arr.index(k)

if index == 0:
    print(f"Nearest greater element is {arr[index+1]}")

elif index == len(arr)-1:
    print(f"Nearest lesser element is {arr[index-1]}")

else:
    print(f"Nearest lesser element is {arr[index-1]}")
    print(f"Nearest greater element is {arr[index+1]}")