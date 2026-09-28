n = int(input("Enter number :"))
ch_1 = 64
ch_2 = 96
for i in range(1,n+1):
    if i%2!=0:
        print(chr(ch_1+i),end=" ")
    else:
        print(chr(ch_2+i),end=" ")