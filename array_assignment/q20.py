print("Find Maximum product contiguous sub array")
arr = [2, 3, 4, 5, -1, 0]
mul = arr[0]

for i in range(len(arr)):

    product = 1

    for j in range(i,len(arr)):

        product = product * arr[j]

        if product > mul:
            mul = product
print(mul)

