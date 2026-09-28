import math

n = int(input("Enter number: "))

for i in range(1, n + 1):

    square = i ** 2
    cube = i ** 3
    root = math.sqrt(i)

    print("Number:", i)
    print("Square:", square)
    print("Cube:", cube)
    print("Square Root:", root)