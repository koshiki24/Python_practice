print("Sort the dictionaries by its value in ascending order")
a = {"a":20,"b":10,"c":40,"d":30}
b = {}
for key in a:
    b[key] = a[key]
for i in b:
    for j in b:
        if b[i] < b[j]:
            t = b[i]
            b[i] = b[j]
            b[j] = t
print(b)

    