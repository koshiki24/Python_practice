quantity = int(input("Enter Quantity :"))
cost = quantity*100
if cost > 100:
 total_cost = cost-cost*(10/100)
 print(f"After discount amount is {total_cost}")
else:
 print(f"Amount is {cost}")