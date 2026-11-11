print("Check whether two strings are equal without using == for the complete strings")
def check(a,b):
    if len(a)!=len(b):
        return "Not Equal"
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                return "Not Equal"
            else:
                return "Equal"
print(check("koshiki","koshikii"))
    