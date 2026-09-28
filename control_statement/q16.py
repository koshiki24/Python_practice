n = int(input("Enter integer :"))
if n%3 == 0:
    for i in range(-n,n+1,3):
        print(i,end=" ")
    print()