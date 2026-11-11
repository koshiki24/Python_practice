print("Find the first non-repeating character in a string.Example: aabbcddee → c")
a = "aabbccddeegf"
result = {}
for ch in a:
    if ch in result:
        result[ch]+=1
    else:
        result[ch] = 1
#print(result)
#print()
for ch in result:
    if result[ch] == 1:
        print(f"First non-repeating character is : {ch}")
        break
else:
    print("There is no repeating character")