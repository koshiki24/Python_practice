print("Find the length of a string without using len().")
# a = "koshiki"
# print(len(a))
def length(a):
    count = 0
    for ch in a:
        count+=1
    return (f"Length of string is {count}")
print(length("koshiki"))