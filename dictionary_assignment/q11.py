print("Create a dictionary from two lists: one list contains keys and the other contains values. Do not use zip().")
a = ["name","age","marks"]
b = ["koshiki",21,90]
d={}
for i in range(len(a)):
    d[a[i]]=b[i]
print(d)