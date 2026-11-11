print('''Check whether two strings are anagrams.Example: "listen" and "silent" → True''')
a = "amma"
b = "amma"
if len(a)!=len(b):
    print("Strings are not anagram")
else:
    for ch in a:
        if a.count(ch) != b.count(ch):
            print("String are not anagram")
            break
    else:
        print("String are anagram")