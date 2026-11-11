print('''Reverse every word without changing the word order.Example: "Python is easy" → "nohtyP si ysae"''')

print("Reverse every word without changing the word order")

a = "Python is easy"
l = a.split()

for i in range(len(l)):
    word = list(l[i])

    left = 0
    right = len(word) - 1

    while left < right:
        word[left],word[right] = word[right],word[left]
        left+=1
        right-=1
    l[i] = "".join(word)
print(" ".join(l))