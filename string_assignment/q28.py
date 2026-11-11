print('''Check whether one string is a rotation of another.Example: "abcd" and "cdab" → True''')
a = "abcd"
b = "cdab"
l = list(a)
#print(l)
for i in range(len(l)):
    for j in range(len(l)-1,0,-1):
        l[j],l[j-1] = l[j-1],l[j]
    #l[0] = g
    #print(l)

    a = "".join(l)
    print(a)

    if a == b:
        print(True)
        break
else:
    print(False)

