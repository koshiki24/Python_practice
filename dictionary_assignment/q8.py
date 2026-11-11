print("Calculate the sum of all numeric values in a dictionary.")
d = {"name":123,"age":21,"marks":90}
sum = 0
for key,value in d.items():
    if type(key) == int:
        sum += key
    elif type(value) == int:
        sum+=value
print(sum)
