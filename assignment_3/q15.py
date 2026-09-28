price = int (input("enter the price of the bike here : "))

if price > 100000:
    print(f"the road tax of the bike is : {price*(15/100)}")

elif price > 50000 and price <= 100000:
    print(f"the road tax of the bike is : {price*(10/100)}")
elif price <= 50000:
    print(f"the road tax of the bike is : {price*(5/100)}")
else:
    print("invalid input")