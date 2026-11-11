print("Check whether two strings are equal without using == for the complete strings")
a = 'hello'
b = 'hello'
# if len(a)!=len(b):
#     print("Not equal")
# else:
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             print("Not equal")
#             break
#     else:
#         print("equal")

if len(a) != len(b):
    print("String are not equal")
else:
    for i in range(len(a)):
        if ord(a[i]) - ord(b[i]):
            print("Not equal")
            break
    else:
        print("Equal")