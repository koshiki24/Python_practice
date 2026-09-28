for i in range(1,8):
    for j in range(1,4):
        if j == 1 :
            print("1",end="")
        elif i == j == 2:
            print("2",end="")
        elif i == 3 and j == 2:
            print("3",end="")
        elif i == 4 and j == 3:
            print("4",end="")
        elif i == 5 and j == 2:
            print("3",end="")
        elif i == 6 and j == 2:
            print("2",end="")
        else:
            print(" ",end="")
    print()
            