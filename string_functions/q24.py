print('''Reverse every word without changing the word order.Example: "Python is easy" → "nohtyP si ysae''')
def reverse(a):
    s = a.split()
    for i in range(len(s)):
        word = list(s[i])
        left = 0
        right = len(word) - 1
        while left < right:
            word[left],word[right] = word[right],word[left]
            left+=1
            right-=1
        s[i] = " ".join(word)
    l = " ".join(s)
    print(s)
a = "Python is easy"
reverse(a)