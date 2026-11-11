print("Count how many times a particular character occurs")
def count(a):
    result = {}
    l = list(a)
    for ch in l:
        if ch in result:
            result[ch]+=1
        else:
            result[ch]=1
    return result
print(count("koshikii"))
