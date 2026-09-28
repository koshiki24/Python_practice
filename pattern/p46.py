ch = 64
for i in range(1,6):
  print(" "*(5-i),end="")
  for j in range(1,i+1):
    print(chr(ch+j),end="")
  print()