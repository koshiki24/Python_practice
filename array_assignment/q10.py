a = [5,8,9,11,12]
b = [3,8,10,12,15]
i = 0
j = 0
union = []
intersection = []
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        if not union or union[-1]!=a[i] or intersection[-1]!=b[j]:
            union.append(a[i])
            intersection.append(b[j])
        i+=1
        j+=1

    elif a[i] < b[j]:
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i+=1
    else:
        if not union or union[-1]!=b[j]:
            union.append(b[j])
        j+=1
while i < len(a):
    if union[-1]!=a[i]:
        union.append(a[i])
    i+=1

while j < len(b):
    if union[-1]!=b[j]:
        union.append(b[j])
    j+=1

print(union)
print(intersection)
