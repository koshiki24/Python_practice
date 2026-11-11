print('''Find all duplicate characters and their frequencies''')
def duplicate(a):
    result = {}
    for ch in a:
        if ch in result:
            result[ch]+=1
        else:
            result[ch] = 1
    flag = False
    for ch in result:
        if result[ch] > 1:
            print(f"{ch} : {result[ch]}")
            flag = True
    if flag == False:
        print("There is no duplicate character")
a = "abccd"
duplicate(a)