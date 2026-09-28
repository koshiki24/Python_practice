for i in range(1, 6):
    #print(" " * (5 - i), end="")
    for k in range(1,5-i):
        print(" ",end="")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    print()