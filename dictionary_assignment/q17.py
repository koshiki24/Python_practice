print("Count the frequency of each number in a list. Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}")
l = [1,2,2,3,1,2]
result = {}
for element in l:
    if element in result:
        result[element]+=1
    else:
        result[element] = 1
print(result)
