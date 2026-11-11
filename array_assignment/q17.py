print("Rearrange the array in alternating positive and negative items")
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
positive = []
negative = []
result = []
for element in arr:
    if element >= 0:
        positive.append(element)
    else:
        negative.append(element)
print(positive)
print(negative)
i = 0
j = 0
while i < len(positive) and j < len(negative):
    result.append(positive[i])
    result.append(negative[j])
    i+=1
    j+=1

while i < len(positive):
    result.append(positive[i])
    i+=1

while j < len(negative):
    result.append(negative[j])

print(result)

            

