print("Convert lowercase characters to uppercase without using upper().s = inDor434e  => INDOR434E")
s = "inDor434e"
result = ""
for ch in s:
    if ord(ch) >= 97 and ord(ch) <= 122:
        ch = chr(ord(ch)-32)
    result = result + ch
print(result)


