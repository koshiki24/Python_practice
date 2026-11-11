
print('''Expand a compressed string.
Example: "a3b2c4" → "aaabbcccc"''')

def expand(a):
    word = ""
    result = ""

    for ch in a:
        if ch.isdigit():
            result += word * int(ch)
            word = ""
        else:
            word += ch

    return result


a = "a3b2c4"
print(expand(a))
