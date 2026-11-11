print("Print left diagonal & right diagonal")
A = [[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(A)):
    for c in range(len(A[r])):
        if r == c or (r == 0 and c == 2) or (r == 2 and c == 0):
            print(A[r][c],end=" ")
        else:
            print("0",end=" ")
    print()