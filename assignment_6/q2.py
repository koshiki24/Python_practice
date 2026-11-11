print("Upper triangle matrix")
A = [[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(A)):
    for c in range(len(A[r])):
        if r == c or r < c:
            print(A[r][c],end = " ")
        else:
            print("0",end = " ")
    print()