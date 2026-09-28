for i in range(1,6):
    for j in range(1,5):
        if j == 1 or j == 4 or i == 3:
            print("*",end="")
        else:
            print(" ",end="")
    print()