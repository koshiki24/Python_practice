print('''Convert lowercase characters to uppercase without using upper().s = inDor434e  => INDOR434E"''')
def uppercase(a):
    result = ""
    for ch in a:
        if ord(ch)>=97 and ord(ch)<=122:
            ch = chr(ord(ch)-32)
        result = result + ch
    return result
print(uppercase("kOShiki123"))