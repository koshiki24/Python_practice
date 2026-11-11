print("Count how many times a particular character occurs")
s = 'hello'
l = list(s)
result = {}
for ch in l:
    if ch in result:
        result[ch]+=1
    else:
        result[ch] = 1
print(result)