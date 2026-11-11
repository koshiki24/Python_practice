print("Remove a particular character from a string without using replace()")
def remove(a):
    b = input("Enter String :")
    result =""
    for ch in a:
        if ch!=b:
            result+=ch
    print(result)
a = "python"
remove(a)
