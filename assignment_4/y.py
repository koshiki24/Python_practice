for i in range(1,6):
    for j in range(1,6):
        if i+j==6 or (i== j and i<4):
            print("*",end="")
        else:
            print(" ",end="")
    print()