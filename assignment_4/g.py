for i in range(1,6):
    for j in range(1,5):
        if (i == 1 and (j == 2 or j == 3)) or (i == 2 and j == 1) or (i == 3 and (j == 3 or j == 4 or j == 1)) or (i == 4 and (j == 3 or j == 4 or j == 1)) or (i == 5 and j >1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
        