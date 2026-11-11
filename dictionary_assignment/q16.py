print("Count the frequency of each character in a string. Example: hello -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}")
s = "hello"
result = {}
for element in s:
    if element in result:
        result[element]+=1
    else:
        result[element] = 1
print(result)