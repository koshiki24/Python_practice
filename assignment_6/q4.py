print("Print row whose sum of element is maximum")
A = [[13,14,15,16],[5,6,7,8],[9,10,11,12]]
max_sum = 0
for r in range(len(A)):
    sum = 0
    for c in range(len(A[r])):
        sum = sum + A[r][c]
    print(sum)

    if sum > max_sum:
        max_sum = sum
        row = r
print(f"Maximum sum is {max_sum}")
print(f"Row : {A[row]}")

