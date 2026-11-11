print(" Find the most frequent character in a string.")
a = "aabbcccd"
result = {}
for ch in a:
    if ch in result:
        result[ch] +=1
    else:
        result[ch] = 1
largest = 0
key = ""
for ch in result:
    if result[ch] > largest:
        largest = result[ch]
        key = ch
print(f"Most frequent character is {key} and its frequency is {largest}")