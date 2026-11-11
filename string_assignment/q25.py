print("Check whether a string contains only digits without using isdigit().")
a = "0"
if a == "":
    print("String is empty")
else:
    for ch in a:
        if ord(ch)<48 or ord(ch)>57:
            print("String does not contain only digits")
            break
    else:
        print("String contains only digits")