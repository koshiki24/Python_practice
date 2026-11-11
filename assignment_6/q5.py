print("Reverse element in a row")
A = [[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(A)):
    left = 0
    right = len(A[r]) - 1
    for c in range(len(A[r])):
        while left <= right:
            A[r][left],A[r][right] = A[r][right],A[r][left]
            left+=1
            right-=1
        print(A[r][c],end = " ")
    print()

    