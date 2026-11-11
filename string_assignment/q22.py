print(" Find the second most frequent character.")
a = "aabbbbbccccd"
result = {}
for ch in a:
    if ch in result:
        result[ch]+=1
    else:
        result[ch] = 1
largest = 0
second_largest = 0
key = ""
for ch in result:
    if result[ch] > largest:
        second_largest = largest
        largest = result[ch]
    elif result[ch] > second_largest:
        second_largest = result[ch]
        key = ch
for ch in result:
    if result[ch] == second_largest:
        key = ch
print(f"Second most frequent character is {key} and its frequency is {second_largest}")

