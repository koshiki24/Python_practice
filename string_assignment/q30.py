print('''Find the longest common prefix among a list of strings.Example: ["flower", "flow", "flight"] → "fl"''')

a = "flower flight flow"
l = a.split()
print(l)

prefix = ""

for i in range(len(l[0])):
    ch = l[0][i]

    for word in l:
        if i >= len(word) or word[i] != ch:
            print(prefix)
            exit()

    prefix += ch

print(prefix)




    