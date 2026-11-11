print('''4. Restaurant Billing System
Beginner–Intermediate
Concepts: Loops, conditions, functions
Requirements
•	Display a menu with item prices.
•	Let customers select items and quantities.
•	Calculate the running bill.
•	Apply discounts based on the bill amount.
•	Calculate the final bill, including tax.
Bonus: Add coupon codes and repeat-order functionality.
''')

def menu():
    menu = {
        "Coffee": {
            "Espresso": 200, "Cappuccino": 210, "Latte": 200,
            "Mocha": 280, "Cold Coffee": 180, "Matcha": 250
        },
        "Shakes": {
            "Blueberry": 150, "Chocolate Shake": 130,
            "Mango Shake": 150, "Strawberry Shake": 150
        },
        "Starters": {
            "Cheese Balls": 250, "Salted Fries": 200,
            "Peri Peri Fries": 220, "Veg Kabab": 200
        },
        "Soups": {
            "Vegetable": 180, "Tomato Soup": 180,
            "Manchow Soup": 200
        },
        "Pizza": {
            "Margherita": 250, "Paneer Pizza": 280,
            "Onion Capsicum Pizza": 200, "Corn Pizza": 220,
            "Cheese Burst Pizza": 300
        },
        "Chinese": {
            "Veg Noodles": 250, "Manchurian": 200,
            "White Sauce Pasta": 180, "Red Sauce Pasta": 250
        }
    }
    return menu


def display_menu(a):
    for category, items in a.items():
        print("\n", category)
        for item, price in items.items():
            print("\t",item, ":", price)


def restaurant_billing():
    a = menu()
    cart = {}
    bill = 0

    display_menu(a)

    while True:
        choice = input("\nEnter item name (or 'done' to checkout): ").strip().title()

        if choice == "Done":
            break

        found = False

        for category in a:
            if choice in a[category]:
                found = True
                price = a[category][choice]

                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    amount = price * quantity
                    bill = bill + amount

                    if choice in cart:
                        cart[choice]["quantity"] += quantity
                        cart[choice]["amount"] += amount
                    else:
                        cart[choice] = {
                            "price": price,
                            "quantity": quantity,
                            "amount": amount
                        }

                    print("Item amount:", amount)
                    print("Running bill:", bill)
                else:
                    print("Quantity must be greater than zero")

                break

        if found == False:
            print("Item not found!")

    if bill == 0:
        print("No items ordered.")
        return

    # Apply discount based on bill amount
    if bill >= 2000:
        discount = bill * 20 / 100
    elif bill >= 1000:
        discount = bill * 10 / 100
    else:
        discount = 0

    # Coupon code
    coupon = input("\nEnter coupon code (or press Enter to skip): ").strip().upper()

    if coupon == "SAVE10":
        discount = discount + (bill - discount) * 10 / 100
        print("Coupon applied: Extra 10% discount")
    elif coupon != "":
        print("Invalid coupon code")

    discounted_bill = bill - discount

    # Tax calculation: 5% on discounted amount
    tax = discounted_bill * 5 / 100
    final_bill = discounted_bill + tax

    # Final bill
    print("\n" + "=" * 45)
    print("              FINAL RESTAURANT BILL")
    print("=" * 45)
    print("Item\t\tPrice\tQty\tAmount")

    for item, details in cart.items():
        print(item, "\t", details["price"], "\t",
              details["quantity"], "\t", details["amount"])

    print("-" * 45)
    print("Subtotal:", bill)
    print("Discount:", round(discount, 2))
    print("Bill after discount:", round(discounted_bill, 2))
    print("Tax (5%):", round(tax, 2))
    print("Final bill:", round(final_bill, 2))
    print("=" * 45)


restaurant_billing()
