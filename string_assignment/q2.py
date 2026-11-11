print(" Check whether a string is a palindrome.")
a = "nitin"
l = list(a)
left = 0
right = len(l)-1
while left < right:
    l[left],l[right] = l[right],l[left]
    left+=1
    right-=1
s = "".join(l)
if a == s:
    print("String is pallindrome")
else:
    print("String is not pallindrome")
