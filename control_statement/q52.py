a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):

    temp = n
    sum = 0

    while temp > 0:
        r = temp % 10
        sum = sum + r ** 3
        temp = temp // 10

    if n == sum:
        print(n)