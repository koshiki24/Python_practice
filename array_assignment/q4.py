print("Write a program to sort the array")
arr = [5,10,2,3,1,8]
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#      if arr[i]>arr[j]:
#         arr[i],arr[j] = arr[j],arr[i]
# print(arr)

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)