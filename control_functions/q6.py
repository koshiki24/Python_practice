'''6. Shopping Cart and Checkout
Intermediate
Concepts: Loops, conditions, functions, lists, dictionaries
Requirements
•	Store products and prices.
•	Allow customers to add items and quantities.
•	Calculate item-wise and total costs.
•	Apply discounts based on purchase value.
•	Generate a final bill.
Bonus: Implement removing an item and checking product availability.
'''
# 6. Shopping Cart and Checkout
# Intermediate
# Concepts: Loops, conditions, functions, lists, dictionaries
# Requirements
# •	Store products and prices.
# •	Allow customers to add items and quantities.
# •	Calculate item-wise and total costs.
# •	Apply discounts based on purchase value.
# •	Generate a final bill.
# Bonus: Implement removing an item and checking product availability.

def data():
    items = {
        "maggie":12,
        "pasta":25,
        "oats":40,
        "sugar":300,
        "bread":20,
        "coffee":400,
        "milk powder":340,
        "green tea":340,
        "sauce":230,
        "jam":34,
        "chocolate":109
    }
    return items

def add_items():
    item = data()
    content = list(item.keys())

    i =1
    for key , value in item.items():
        print(f"press {i} for - {key} : {value}")
        

        i+=1
    print()
    item_list = {}
    f = True
    while(f):
        print(f"Press 1 to add the elements ")
        print(f"Press 2 if you want to see the total bill after discount ")
        
        print(f"Press 3 for exit()")
        print()
        n = int(input("Enter your choice here : "))

        if n == 1:
            print()
            x = int(input("Eneter the id of item: "))
            if 1<=x<=len(content) :

                quantity = int(input("Enter the quantity of the item :"))
                if quantity>0:
                    item_list[x] = item_list.get(x,0)+quantity
            
                else:
                    print("quantity must be greater than Zero")

            else:
                print("invalid item ID")
        elif n==2:
            total=0
            for i in item_list:
                product_name = content[i-1]
                price = item[product_name]
                quantity = item_list[i]
                total = total + (price * quantity)
            if total >=10000:#20% discount
                final = total-(total/20)
            elif total >=5000: # 10%discount
                final =total-( total/10)
            elif total <5000: # 5%discount
                final = total-(total/20)
            
            print("\n________________________________Bill Is_____________________________")
            print("\nTotal no. of items and their quantitiy is : ")
            print("\nproduct\t\tprice\t\tquantity")
            for i in item_list:
                product_name = content[i-1]
                print(f"{product_name}",end="")

                price = item[product_name]
                print(f"\t\t{price}",end="")

                quantity = item_list[i]
                print(f"\t\t{quantity}",end="")
                print()

            print(f"\nTotal bill is : {total}")
            print()
            print(f"Final bill is : {final}")
            print("\n______________________________________________________________________")

        elif n == 3:

            f = False
        else:
            print("Please enter a valid choice ")
                    

add_items()