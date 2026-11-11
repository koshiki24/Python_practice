print('''Remove duplicate characters while preserving their original order.Example: "programming" → "progamin"''')
a = "programming"
result = {}
for ch in a:
    if ch in result:
        result[ch] = 1
    else:
        result[ch] = 1
#print(result)
s = "".join(result)
print(s)