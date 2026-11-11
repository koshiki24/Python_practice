print('''Safely retrieve a value from a deeply nested dictionary. If any key is
    missing, return a default value such as "Unknown".''')
a = {
    "student" : {
        "name":{
            "id":100
            }
        }
}
keys = ["student","name","id"]
for key in keys:
    if key in a:
        a = a[key]
    else:
        a = "unknown"
        break
print(a)
