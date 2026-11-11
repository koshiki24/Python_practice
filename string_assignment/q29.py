print("Remove a particular character from a string without using replace().")
a = "python"
b = input("Enter character you want to remove :")
result = ""
for ch in a:
    if ch!=b:
        result+=ch
print(result)
