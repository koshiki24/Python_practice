'''for i in range(1,6):
    for j in range(1,6):
        if (i == 1 and j == 3) or (i == 2 and (j == 2 or j == 4)) or (i == 3) or (i == 4 or i == 5) and (j == 1 or j == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''


'''for i in range(1,6):
  for j in range(1,2*i):
    if (i + j == 6) or (j-i == 3) or (i == 3 and (j >=3 and j <= 7)):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print() '''

for i in range(1,6+1):
    for j in range(1, 9+1):
        if (i + j == 6) or (j - i == 3) or (i == 3 and (j > 3 and j < 7)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()