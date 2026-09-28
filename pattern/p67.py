for i in range(1,6):
    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j == 3:
            print("#",end="")
        else:
            print("*",end="")
    print()