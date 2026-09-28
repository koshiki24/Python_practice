for i in range(1,7):
    for j in range(1,7):
        if (i == 1 and j>1 and j<5) or (i == 5 and j>1 and j<5) or (j==1 and i>1 and i<5) or (j==5 and i>1 and i<5) or (i == 6 and j == 6) or (i == 3 and j == 3):
            print("*",end="")
        else:
            print(" ",end="")
    print()