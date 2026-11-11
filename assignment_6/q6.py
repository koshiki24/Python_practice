print("Swap row whose sum is maximum with a row whose sum is minimum")
A = [[1,2,3],[4,5,6],[7,8,9]]
maximum = 0
minimum = 0
for r in range(len(A)):
    sum = 0
    for c in range(len(A[r])):
        sum = sum + A[r][c]
    print(sum)

    if r == 0:
        minimum = sum
        maximum = sum
        min_row = r
        max_row = r
    else:
        if minimum > sum:
            minimum = sum
            min_row = r
        if maximum < sum:
            maximum = sum
            max_row = r
print(minimum)
print(maximum)
A[min_row],A[max_row] = A[max_row],A[min_row]
print(A)
    
