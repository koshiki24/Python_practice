for i in range(1,6):
    for j in range(11):
        if j == 0 or j == 10 or i==j or i+j==10:
            print("*",end="")
        else:
            print(" ",end="")
    print()