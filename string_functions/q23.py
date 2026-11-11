print('''Reverse the order of words in a sentence.Example: "Python is easy" → "easy is Python''')
def order(a):
    l = a.split()
    left = 0
    right = len(l) - 1
    while left < right:
        l[left],l[right] = l[right],l[left]
        left+=1
        right-=1
    s = " ".join(l)
    print(s)
a = "Python is easy"
order(a)