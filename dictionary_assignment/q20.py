print("Reverse a dictionary so that values become keys and keys become values.Assume all values are unique.")
a = {"a":10,"b":20,"c":30}
b = {}
for key,value in a.items():
    b[value] = key
print(b)
    
