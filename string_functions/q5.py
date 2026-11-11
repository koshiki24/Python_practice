print("Count the number of words in a sentence.")
def count(a):
    s = a.split()
    return(f"Number of words : {(len(s))}")
print(count(" I am koshiki "))