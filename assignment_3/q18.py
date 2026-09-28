unit = float (input("Enter the number here "))
amount =0
if unit<=50:
    amount = unit*0.5
elif unit<= 150:
    amount = (50 * 0.50) + ((unit - 50) * 0.75)
elif unit <=250:
    amount = (50 * 0.50) + (100 * 0.75) + ((unit - 150) * 1.20)
else:
    amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit- 250) * 1.50)


charges = amount * 0.2

bill = amount + charges
print(f"amount : {amount}")
print(f"surcharge (20%) is : {charges}")
print(f'Total Bill is : {bill}')