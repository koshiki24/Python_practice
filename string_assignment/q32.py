print('''Find the longest palindromic substring.
Example: "babad" → "bab" or "aba"''')
a = "abcde"
longest = ""
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        sub = a[i:j]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub
if longest == "":
    print("There is no longest substring")
else:
    print(f"Longest pallindromic string is : {longest}")

