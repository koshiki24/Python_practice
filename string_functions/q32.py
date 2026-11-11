print('''Find the longest palindromic substring.
Example: "babad" → "bab" or "aba"''')

def pallindrome(a):
    b = ""

    for i in range(len(a)):
        for j in range(i, len(a)):
            sub = a[i:j+1]

            if sub == sub[::-1]:
                if len(sub) > len(b):
                    b = sub

    return b

a = "babad"
print(pallindrome(a))
