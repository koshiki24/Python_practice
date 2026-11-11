print('''Check whether a string contains only digits without using isdigit()''')
def digit(a):
    if a == "":
        print("String is empty")
    else:
        for ch in a:
            if ord(ch) < 48 or ord(ch) > 57:
                print("String does not contain only digit")
                break
        else:
            print("String contain only digit")
a = "12345A"
digit(a)