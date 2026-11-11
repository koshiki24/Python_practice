print("Peak an element")
arr = [12,3,4,5,6,8,10]
for i in range(len(arr)):
    if i == 0:
        if arr[i] > arr[i+1]:
            print(f"Peak element is : {arr[i]}")
            break

    elif i == len(arr)-1:
        if arr[i] > arr[i-1]:
            print(f"Peak element is : {arr[i]}")
            break

    elif i > 0 and i < len(arr)-1:
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            print(f"Peak element is : {arr[i]}")
            break

else:
    print("There is no peak element")
        


        