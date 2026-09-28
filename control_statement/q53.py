a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):

    temp = n
    sum = 0

    while temp > 0:

        r = temp % 10

        fact = 1
        for i in range(1, r + 1):
            fact = fact * i

        sum = sum + fact
        temp = temp // 10

    if sum == n:
        print(n)