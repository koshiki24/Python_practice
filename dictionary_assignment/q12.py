print("Print all keys, all values, and all key-value pairs of a dictionary.")
d = {"a":10,"b":15,"c":20}
print("All keys are : ",end=" ")
for key in d.keys():
    print(key,end=" , ")

print("\nAll values are : ",end=" ")
for value in d.values():
    print(value,end=" , ")
print("\nAll key, value pairs are : ",end=" ")
for key,value in d.items():
    print(f"({key},{value})",end=" , ")