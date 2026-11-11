print("Replace every space with a hyphen (-)")
def replace(a):
    result = ""
    for ch in a:
        if ch == " ":
            result = result+"-"
        else:
            result = result+ch
    return result
print(replace("I am koshiki"))