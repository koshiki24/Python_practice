print('''Find the second most frequent character.''')
def second(a):
    result = {}
    for ch in a:
        if ch in result:
            result[ch]+=1
        else:
            result[ch]=1
    largest = 0
    second_largest = 0
    key = ""
    for ch in result:
        if result[ch] > largest:
            second_largest = largest
            largest = result[ch]
            key = ch
        elif result[ch] > second_largest and result[ch] < largest:
            second_largest = result[ch]
            key = ch
    print(f"Second largest element is {key} and it's frequency is {second_largest}")
    
    print
a = "abbccc"
second(a)