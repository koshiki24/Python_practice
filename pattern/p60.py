for i in range(1,6):
  print(" "*(5-i),end=" ")
  for j in range(1,i+1):
    if i == 3 and j == 2:
      print("_",end=" ")
    elif i == 4 and (j == 2 or j == 3):
      print("_",end=" ")
    else:
      print("X",end=" ")
  print()