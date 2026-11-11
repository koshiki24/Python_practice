print("Find the longest word in a sentence.")
a = "Python is easy"
l = a.split()
print(l)
largest = ""
for i in range(len(l)):
    word = list(l[i])
    if len(l[i]) > len(largest):
        largest = l[i]
print(largest)