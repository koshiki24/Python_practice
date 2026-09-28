a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):

    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        print(n)