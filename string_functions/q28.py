print('''Check whether one string is a rotation of another.Example: "abcd" and "cdab" → True''')
def rotation(a):
    l = list(a)
    b = "cdab"
    for i in range(len(l)):
        first = l[0]
        for j in range(len(l)-1):
            l[j] = l[j+1]
        l[len(l)-1] = first

        a = "".join(l)
        print(a)

        if a == b:
            print(True)
            break
    else:
        print(False)
a = "abcd"
rotation(a)
            
