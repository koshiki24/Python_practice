print("1\n10\n101\n1010\n10101")
n = int(input("Enter terms :"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j % 2,end = " ")
  print()