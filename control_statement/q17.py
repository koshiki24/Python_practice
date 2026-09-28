n = int(input("Enter the number of terms: "))

num = 1
add = 1

for i in range(n):
    print(num, end=" ")
    num = num + add
    add = add + 1