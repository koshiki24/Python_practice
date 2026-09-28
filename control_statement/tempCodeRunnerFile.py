a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):

    temp = n
    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + r ** 3
        n = n // 10

    if temp == sum:
        print(temp)