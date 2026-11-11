print("Replace every space with a hyphen (-)")
s = "I am koshiki  sharma  "
result = ""
# s = "-".join(s.split())
# print(s)

for ch in s:
    if ch == " ":
        result = result+"-"
    else:
        result = result+ch

print(result)