print('''Create a new dictionary containing only entries whose values are greater
    than or equal to a given threshold. Do not modify the dictionary while
    iterating over it.''')
a = {"apple" : 20 , "banana": 30 , "cherry" : 40 , "grapes" : 50}
threshold = int(input("Enter threshold : "))
b = {}
for key,value in a.items():
    if value >= threshold:
        b[key] = value
if len(b) == 0:
    print("No value found")
else:
    print(b)