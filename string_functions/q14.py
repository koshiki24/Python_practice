print("Remove all digits from a string")
def remove(a):
    result = ""
    for ch in a:
        if ord(ch)<48 or ord(ch)>57:
            result = result + ch
    return result
print(remove("abc123de"))
