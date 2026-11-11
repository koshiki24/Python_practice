print('''Check whether two strings are anagrams.Example: "listen" and "silent" → True''')
def anagram(a,b):
    if len(a)!=len(b):
        return "Not anagram"
    else:
        for ch in a:
            if a.count(ch)!=b.count(ch):
                return "Strings are not anagram"
        else:
            return "String are anagram"
print(anagram("amma","amma"))
            