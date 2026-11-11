print("Find all duplicate characters and their frequencies")
a = "progaminn"
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
    print("Every character is non repeating")
    