print("Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a python program to produce third array C by merging arrays A and B in ascending order")

a = [1, 2, 3, 4, 9, 10, 20]
b = [50, 42, 35, 28, 19, 12, 7, 3]
c = []
c = a + b
print(f"Array after concatenation : {c}")
for i in range(len(c)-1):
    for j in range(i+1,len(c)):
        if c[i] > c[j]:
            c[i],c[j] = c[j],c[i]
print(f"Array after swapping : {c}")
