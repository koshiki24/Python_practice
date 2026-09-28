for i in range(1,6):
  print(" "*(5-i),end="")
  for j in range(1,i+1):
    if j%2==0:
      print("0",end="")
    else:
      print("1",end="")
  print()