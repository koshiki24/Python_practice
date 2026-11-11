print('''Find the longest common prefix among a list of strings.Example: ["flower", "flow", "flight"] → "fl"''')


def split(a):
    prefix = ""

    for i in range(len(a[0])):
        ch = a[0][i]

        for word in a:
            if i >= len(word) or word[i] != ch:
                return prefix

        prefix += ch

    return prefix


a = ["flower", "flow", "flight"]
print(split(a))






    