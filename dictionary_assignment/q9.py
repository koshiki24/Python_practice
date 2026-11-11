print("Find the key associated with the largest value in a dictionary.")
d = {"apple" : 100 , "banana" : 1500 , "cherry" : 200}
largest = 0
key_value = ""
for key,value in d.items():
    if value > largest:
        largest = value
        key_value = key
print(key_value)