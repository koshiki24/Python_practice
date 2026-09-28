for i in range(1,6):
    for j in range(1,10):
        if i+j == 6 or j-i == 4 or j == 1 or j == 9:
            print("*",end="")
        else:
            print(" ",end="")
    print()