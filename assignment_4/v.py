for i in range(1,5):
    for j in range(1,8):
        if i == j or i+j == 8:
            print("*",end="")
        else:
            print(" ",end="")
    print()