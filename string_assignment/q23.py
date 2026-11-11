print('''Reverse the order of words in a sentence.Example: "Python is easy" → "easy is Python"''')
a = "Python is easy"
l = a.split()
#print(l)
left = 0
right = len(l)-1
while left < right:
    l[left],l[right] = l[right],l[left]
    left+=1
    right-=1
#print(l)
s = " ".join(l)
print(s)