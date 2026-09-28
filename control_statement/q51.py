a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):

    temp = n
    rev = 0

    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10

    print(rev)