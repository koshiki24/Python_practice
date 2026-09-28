ch = 64
for i in range(1,10,2):
  print(" "*(10-i),end=" ")
  for j in range(1,i+1):
    print(chr(ch+j),end=" ")
  print()