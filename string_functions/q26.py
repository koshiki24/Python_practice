print('''Find the longest word in a sentence.''')
def length(a):
    l = a.split()
    longest = ""
    for i in range(len(l)):
        if len(l[i]) > len(longest):
            longest = l[i]
    print(longest)
a = "Python is easy"
length(a)
    