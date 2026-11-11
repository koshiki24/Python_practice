print('''Check whether a string has balanced parentheses.[Stack]Example: "{[()]}" → True, "([)]" → False''')
a = "{[()]})"
b = []
for ch in a:
    if ch == '(' or ch == '[' or ch == '{':
        b.append(ch)
    else:
        if len(b) == 0:
            print(False)
            break
        last = b.pop()

        if (last == ')' and ch !='(') or (last == '}' and ch != '{') or (last == ']' and ch != '['):
            print(False)
            break
else:
    if len(b) == 0:
        print(True)
    else:
        print(False)
