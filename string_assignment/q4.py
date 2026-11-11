print("Count uppercase letters, lowercase letters, digits, and special characters.")
a = "koshikiAB12@#"
upper_case = lower_case = digit = sc = 0
for ch in a:
    if ord(ch)>=65 and ord(ch)<=90:
        upper_case+=1
    elif ord(ch)>=97 and ord(ch)<=122:
        lower_case+=1
    elif ord(ch)>=48 and ord(ch)<=57:
        digit+=1
    else:
        sc+=1
print(f"Upper case character is : {upper_case}")
print(f"Lower case character is : {lower_case}")
print(f"Digit character is : {digit}")
print(f"special symbol character is : {sc}")