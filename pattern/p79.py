for i in range(1,5):
    for k in range(4-i,0,-1):
        print(" ",end="")
    for j in range(1,2*i):
        if (i%2!=0 and j%2!=0):
            print("*",end="")
        else:
            print("_",end="")
        if (i%2==0 and j%2!=0):
            print("*",end="")
        else:
            print("_",end="")
        
    print()
'''for i in range(3,0,-1):
    for k in range(4-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()'''