ch = 64
for i in range(5,0,-1):
    for k in range(5-i,0,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(ch+j),end=" ")
    print()