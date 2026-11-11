print("Write a program to reverse a string without using slicing")
a = "hello"
b = list(a)
print(b)
left = 0
right = len(b)-1
while left < right:
        b[left],b[right] = b[right],b[left]
        left+=1
        right-=1
a = " ".join(b)
print(a)
