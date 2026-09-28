for i in range(1,6):
    for j in range(1,6):
        if (i == 1 and j>1 and j<5) or (i == 5 and j>1 and j<5) or (j == 1 and i>1 and i<5) or (j == 5 and i>1 and i<5):
            print("*",end="")
        else:
            print(" ",end="")
    print()