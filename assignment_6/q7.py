# print("Transpose of a matrix")
# A = [[1,2,3],[4,5,6],[7,8,9]]
# for r in range(len(A)):
#     for c in range(len(A[r])):
#         if r < c:
#          A[r][c],A[c][r] = A[c][r],A[r][c]
#         print(A[r][c],end=" ")
#     print()

print("Transpose of a matrix")
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[0]*3,[0]*3,[0]*3]
# for r in range(len(A)):
#     for c in range(len(A[r])):
#        if r < c:
#           A[r][c],B[c][r] = B[c][r],A[r][c]
#        print(B[r][c],end=" ")
#     print()


for i in range(len(A)):
   for j in range(len(A[i])):
      B[j][i] = A[i][j]
print(B)
