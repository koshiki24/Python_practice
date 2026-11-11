print("Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a java program to produce third array Z by merging arrays X and Y in descending order")
a = [50, 42, 35, 28, 19, 12, 7]
b = [20, 10, 9, 4, 3, 2, 1]
c = []
c = a + b
print(c)

for i in range(len(c)-1):
    for j in range(i+1,len(c)):
        if c[i] < c[j]:
            c[i],c[j] = c[j],c[i]

print(f"After sorting : {c}")

