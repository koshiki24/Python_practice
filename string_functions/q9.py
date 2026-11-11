print("Find the first and last character of a string")
def first_last(a):
    l = list(a)
    return(f"first character is {l[0]}\nlast character is {l[len(l)-1]}")
print(first_last("koshiki"))