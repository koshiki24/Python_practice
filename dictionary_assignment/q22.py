print("Find the common key between two dictionaries")
a = {"a":10,"b":20}
b = {"b":20,"c":30}
for element in a:
    if element in b:
        print(element)