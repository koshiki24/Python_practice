print('''Group a list of words according to their length.Example: ["cat", "apple", "dog", "mango"] Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]''')
print("Group words according to their length")

a = ["cat", "apple", "dog", "mango","that"]
b = {}

for i in range(len(a)):
    count = len(a[i])

    if count not in b:
        b[count] = []
    b[count].append(a[i])
print(b)