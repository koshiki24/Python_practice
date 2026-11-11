print("Find the second-largest distinct value in a dictionary")
data = {
    'a':10,
    'b':30,
    'c':20,
    'd':50,
    'e':2
}
largest = 0
second_largest = 0
for value in data.values():
    if len(data) < 2:
        print("Maybe list is empty or there is only one element in the list so second largest is not possible")
    elif largest == 0 or largest < value:
        second_largest = largest
        largest = value
    elif value < largest and value > second_largest:
        second_largest = value
if second_largest == 0:
    print("Second largest distinct value does not exist")
else:
    print("Second largest distinct value is :",second_largest)
