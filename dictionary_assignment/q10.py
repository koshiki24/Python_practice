print("Merge two dictionaries. If a key exists in both dictionaries, use the value from the second dictionary.")
a = {"a":10,"b":20}
b = {"a":15,"b":25,"c":30}
for key,value in b.items():
    a[key] = value
print(a)
        