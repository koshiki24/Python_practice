ch = 64
for i in range(5,0,-1):
  for j in range(1,i+1):
    if i == 1 or j == i or i == 5 or j == 1:
      print(chr(ch+j),end=" ")
    else:
      print(" ",end=" ")
  print()