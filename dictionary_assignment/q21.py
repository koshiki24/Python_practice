print('''Combine two dictionaries by adding the values of common keys.
    Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
    Expected: {'a': 10, 'b': 25, 'c': 7}''')
c = {"a":10,"b":20}
d = {"b":5, "c":7}
for element in d:
    if element in c:
        c[element] = c[element] + d[element]
    else:
        c[element] = d[element]
print(c)
