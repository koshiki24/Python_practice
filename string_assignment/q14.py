print("Remove all digits from a string")
s = "indore123"
result = ""
for ch in s:
    if ord(ch) < 48 or ord(ch) > 57:
        result = result + ch
print(result)