
print('''Check whether a string has balanced parentheses.
Example: "{[()]}" → True, "([)]" → False''')

def balanced(a):
    b = []

    for ch in a:
        if ch == '(' or ch == '[' or ch == '{':
            b.append(ch)
        else:
            if len(b) == 0:
                return False

            last = b.pop()

            if (last == '(' and ch != ')') or \
               (last == '{' and ch != '}') or \
               (last == '[' and ch != ']'):
                return False

    if len(b) == 0:
        return True
    else:
        return False


a = "{[()]}"
print(balanced(a))
