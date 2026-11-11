print('''Group words that are anagrams of one another. Example: ["eat", "tea", "bat", "ate"] Expected groups: ["eat", "tea", "ate"] and ["bat"]''')
a = ["eat","tea","bat","ate"]
used = []
result = []
for i in range(len(a)):
    if a[i] not in used:
        group = [a[i]]
        used.append(a[i])

        for j in range(i+1,len(a)):
            if sorted(a[i]) == sorted(a[j]):
                group.append(a[j])
                used.append(a[j])
        result.append(group)
print(result)