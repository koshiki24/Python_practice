print('''Count the frequency of every character using a dictionary. Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}''')
a = "hello"
result = {}
for ch in a:
    if ch in result:
        result[ch]+=1
    else:
        result[ch] = 1
print(result)