n = int(input("Enter number: "))

temp = n
last = n % 10

count = 0
while n > 0:
    count = count + 1
    n = n // 10

first = temp // (10 ** (count - 1))

middle = (temp % (10 ** (count - 1))) // 10

result = last * (10 ** (count - 1)) + middle * 10 + first

print("After interchange:", result)