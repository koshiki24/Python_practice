print("Find all duplicate elements in a list and their frequencies.")
l = [1,2,5,6,4,3,1,5,6,4,3]
a = {}
for element in l:
    if element in a:
        a[element]+=1
    else:
        a[element]=1
print(a,end=" ")
print()
for element in a:
    if a[element] > 1:
        print(element,end=" ")