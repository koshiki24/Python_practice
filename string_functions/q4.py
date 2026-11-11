print("Count uppercase letters, lowercase letters, digits, and special characters.")
def count(a):
    upper = lower = digit = sc = 0
    for ch in a:
        if ord(ch) >= 65 and ord(ch) <= 90:
            upper+=1
        elif ord(ch) >= 97 and ord(ch) <= 122:
            lower += 1
        elif ord(ch) >= 48 and ord(ch) <= 57:
            digit+=1
        else:
            sc+=1
    return (f"Upper count is {upper}\nLower count is {lower}\nDigit count is {digit}\nSpecial character count is {sc}")
print(count("KoShiki2409+@#$"))

