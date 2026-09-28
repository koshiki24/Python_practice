ch = 96

for i in range(1, 6):
    for j in range(1, i + 1):
        ch += 1

        if j == 1 or j == i or i == 5:
            print(chr(ch), end="")
        else:
            print(" ", end="")
    print()