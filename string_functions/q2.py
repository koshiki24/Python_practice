print("Check whether a string is a palindrome")
def pallindrome(a):
    b = list(a)
    left = 0
    right = len(b)-1
    while left < right:
        b[left],b[right] = b[right],b[left]
        left+=1
        right-=1
    s = "".join(b)

    if a == s:
        return "Pallindrome"
    else:
        return "Not pallindrome"
print(pallindrome("nitinn"))