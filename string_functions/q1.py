print("Write a program to reverse a string without using slicing")
# def reverse(a):
#     result = ""
#     for ch in a:
#         result = ch + result
#     return result
# print(reverse("hello"))
def reverse(a):
    b = list(a)
    left = 0
    right = len(a)-1
    while left < right:
        b[left],b[right] = b[right],b[left]
        left+=1
        right-=1
    s = "".join(b)
    return s
print(reverse("hello"))
