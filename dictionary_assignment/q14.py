print("Copy a dictionary into another dictionary. Explain whether changing nested object in the copy can affect the original.")
a = {"name":"koshiki","age":21,"marks":90}
b = a
b["marks"] = 80
print(a)
print(b)