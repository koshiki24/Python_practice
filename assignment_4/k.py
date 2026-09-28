for i in range(1,6):
    for j in range(1,4):
        if j == 1 or (i == 2 and j == 2) or (i == 1 and j == 3) or (i == 4 and j == 2) or (i == 5 and j == 3):
            print("*",end="")
        else:
            print(" ",end="")
    print()