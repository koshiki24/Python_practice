salary = int(input("Enter your salary :"))
year = int(input("Enter year of services :"))
if year > 5:
 bonous = salary*(5/100)
else:
 bonous = salary*(0/100)
print(f"net bonous is {bonous}")