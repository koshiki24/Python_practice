a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for n in range(a, b + 1):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print(n, "=", fact)