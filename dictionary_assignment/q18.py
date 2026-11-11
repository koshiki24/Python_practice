print("Find the first non-repeating character in a string using a dictionary.")
a = "ababccde"
result = {}

for element in a:
    if element in result:
        result[element]+=1
    else:
        result[element] = 1

for element in a:
    if result[element] == 1:
        print(element)
        break
    
else:
    print("All character are repeating")
