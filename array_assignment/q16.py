print("Sub with equal 0s and 1s")
arr = [1,0,0,1,0,1,1]
count = 0
for i in range(len(arr)):
    zero = 0
    one = 0
    for j in range(i,len(arr)):
        if arr[j] == 0:
            zero+=1
        else:
            one+=1
        if zero == one:
            count+=1
print(count)