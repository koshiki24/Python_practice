print("Remove all spaces from a string.")
s = "I am koshiki"
for ch in s:
    if ch == " ":
        s = s.replace(" ","")
print(s)
