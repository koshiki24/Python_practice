print('''Compress a string by counting consecutive repeated characters.
Example: "aaabbccccd" → "a3b2c4d1"''')
a = "aaabbccccd"
b = ""
count = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count+=1
    else:
        b+=a[i]+str(count)
        count = 1
b+= a[len(a)-1]+str(count)
print(b)
    