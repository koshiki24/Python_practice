print('''Given two arrays of integers A and B of sizes M and N respectively. Write a Write a java program, which will produce a third array named C. such that the following sequence is followed. 
All even numbers of A from left to right are copied into C from left to right. 

All odd numbers of A from left to right are copied into C from right to left. 
All even numbers of B from left to right are copied into C from left to right. 
All old numbers of B from left to right are copied into C from right to left.
e.g., A is {3, 2, 1, 7, 6, 3} and B is {9, 3, 5, 6, 2, 8, 10} the resultant array C is {2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3} 
''')
a = [3, 2, 1, 7, 6, 3]
b = [9, 3, 5, 6, 2, 8, 10]
c = []
a_even = []
a_odd = []
b_even = []
b_odd = []
for i in range(len(a)):
    if a[i]%2 == 0:
        a_even.append(a[i])
    else:
        a_odd.append(a[i])
print(a_even)
print(a_odd)

for j in range(len(b)):
    if b[j]%2 == 0:
        b_even.append(b[j])
    else:
        b_odd.append(b[j])
print(b_even)
print(b_odd)

left = 0
right = len(b_odd)-1
while left < right:
    b_odd[left],b_odd[right] = b_odd[right],b_odd[left]
    left +=1
    right-=1
print(b_odd)

left = 0
right = len(a_odd)-1
while left < right:
    a_odd[left],a_odd[right] = a_odd[right],a_odd[left]
    left +=1
    right-=1
print(a_odd)

c = a_even + b_even + b_odd + a_odd
print(c)