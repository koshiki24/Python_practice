print("Remove a key from a dictionary using pop(). Handle the case where the key does not exist.")
d = {"name":"koshiki","age":21,"marks":90}
if "marks" in d:
    d.pop("marks")
    print(d)
else:
    print("Marks does not exist")