n = int(input("Enter decimal number: "))

binary = 0
place = 1

while n > 0:
    r = n % 2
    binary = binary + r * place
    place = place * 10
    n = n // 2

print("Binary number:", binary)