print('''Find the first repeating character.Example: "programming" → r''')
a = "programming"
result = {} 
for ch in a:
    if ch in result:
        result[ch]+=1
    else:
        result[ch] = 1
for ch in result:
    if result[ch] > 1:
        print(f"First repeating character is : {ch}")
        break
else:
    print("There is no repeating character")