print('''Expand a compressed string.
Example: "a3b2c4" → "aaabbcccc"''')
a = "a3b2c4"
word = ""
result = ""
for ch in a:
    if ch.isdigit():
        result += word * int(ch)
        word = ""
    else:
        word+=ch
print(result)
