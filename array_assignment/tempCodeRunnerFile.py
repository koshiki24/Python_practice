print("Max Sum in configuration")
arr = [8,3,1,2]
# left = 0
# max = 0
# for j in range(len(arr)-1,-1,-1):
#     right = len(arr)-1
#     a = arr[right]
#     for i in range(len(arr)-1,-1,-1):
#         arr[i] = arr[i-1]
#     arr[0] = a
    

#     sum = 0
#     for k in range(len(arr)):
#         sum += arr[k] * k
    

    
#     if sum > max:
#         max = sum
# print(max)

left = 0
max = 0
for j in range(len(arr)-1,-1,-1):
    right = len(arr)-1
    a = arr[right]
    for i in range(len(arr)-1,-1,-1):
        arr[i] = arr[i-1]
    arr[0] = a

    sum = 0
    for k in range(len(arr)):
        sum+=arr[k]*k

    if sum > max:
        max = sum
print(max)

