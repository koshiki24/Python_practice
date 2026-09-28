ch = 64
for i in range(5,0,-1):
  print(" "*(5-i),end="")
  for j in range(1,i+1):
    if i == 4 and (j == 2 or j == 3):
      print("_",end="")
    elif i == 3 and j == 2:
      print("_",end="")
    else:
      print(chr(ch+j),end="")
  print()