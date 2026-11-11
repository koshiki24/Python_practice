print("Given two dictionaries, return the keys whose values are equal in both.")
a = {"a":10,"b":30,"c":20}
b = {"a":10,"b":15,"c":20}
for key in a:
    if key in b and a[key] == b[key]:
        print(key,end=" ")