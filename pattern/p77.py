for i in range(1,5):
    for k in range(4-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
    temp = 1
for i in range(3,0,-1):
    for k in range(1,temp+1):
        print(" ",end="")
    temp+=1
    for j in range(1,i+1):
        print(j,end="")
    print()
    