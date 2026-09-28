print("Welcome! To D-mart")
name = input("Enter your name : ")
gender = input("Enter your gender : ")
item1 = input("Enter your 1st item :")
qty1 = int(input("Enter quantity of 1st item :"))
item2 = input("Enter your 2nd item :")
qty2 = int(input("Enter quantity of 2nd item :"))
item3 = input("Enter your 3rd item :")
qty3 = int(input("Enter quantity of 3rd item :"))
item4 = input("Enter your 4th item :")
qty4 = int(input("Enter quantity of 4th item :"))
item5 = input("Enter your 5th item :")
qty5 = int(input("Enter quantity of 5th item :"))
item6 = input("Enter your 6th item :")
qty6 = int(input("Enter quantity of 6th item :"))
item7 = input("Enter your 7th item :")
qty7 = int(input("Enter quantity of 7th item :"))
item8 = input("Enter your 8th item :")
qty8 = int(input("Enter quantity of 8th item :"))
item9 = input("Enter your 9th item :")
qty9 = int(input("Enter quantity of 9th item :"))
item10 = input("Enter your 10th item :")
qty10 = int(input("Enter quantity of 10th item :"))
cost_item1 = 10*qty1
cost_item2 = 20*qty2
cost_item3 = 30*qty3
cost_item4 = 40*qty4
cost_item5 = 50*qty5
cost_item6 = 60*qty6
cost_item7 = 70*qty7
cost_item8 = 80*qty8
cost_item9 = 90*qty9
cost_item10 = 100*qty10
if qty1 > 4:
 cost1_d = cost_item1 - cost_item1*(5/100)
cost5_d = cost_item5 - cost_item5*(10/100)
cost10_d = cost_item10 - cost_item10*(15/100)
total_amount = cost1_d + cost_item2 + cost_item3 + cost_item4 + cost5_d + cost_item6 + cost_item7 + cost_item8 + cost_item9 + cost10_d
total_amount_after_discount = total_amount - (cost1_d + cost5_d + cost10_d)
gst = total_amount*(10/100)
total_amount = total_amount + gst
carry_bag = input("Do you need carry bag? (Y/N)")
if carry_bag == 'Y':
 total_amount = total_amount + 10
else:
 total_amount = total_amount+0
if total_amount > 10000:
 total_amount_dis = total_amount - total_amount*(15/100)
if total_amount >=5000 and total_amount <= 1000:
 total_amount_discount = total_amount - total_amount*(10/100)
if gender == 'female':
 gift = 'Cadburry'
 print(gift)
else:
 gift = 'Leather Wallet'
 print(gift)


print("                                        D-Mart                                                            ")
print(f"Name:- {name}                                                    Date:-15/09/2026")
print("-----------------------------------------------------------------------------------")
print(f"Item-Name\tQuantity\tPrice\tTotal\tAfter-Discount")
print(f"{item1} \t\t {qty1} \t\t {cost_item1} \t 10 \t {cost1_d}")
print(f"{item2} \t\t {qty2} \t\t {cost_item2} \t 20 \t {cost_item2}")
print(f"{item3} \t\t {qty3} \t\t {cost_item3} \t 30 \t {cost_item3}")
print(f"{item4} \t\t {qty4} \t\t {cost_item4} \t 40 \t {cost_item4}")
print(f"{item5} \t\t {qty5} \t\t {cost_item5} \t 50 \t {cost5_d}") 
print(f"{item6} \t\t {qty6} \t\t {cost_item6} \t 60 \t {cost_item6}")
print(f"{item7} \t\t {qty7} \t\t {cost_item7} \t 70 \t {cost_item7}")
print(f"{item8} \t\t {qty8} \t\t {cost_item8} \t 80 \t {cost_item8}")
print(f"{item9} \t\t {qty9} \t\t {cost_item9} \t 90 \t {cost_item9}")  
print(f"{item10} \t\t {qty10} \t\t {cost_item10} \t 100 \t {cost10_d}") 
print("-----------------------------------------------------------------------------------")
print(f"   \t   \t   \t        A.P \t       D.P")
print(f"   \t   \t   \t        {total_amount} \t {total_amount_after_discount}")
print(f"Gift :- {gift} \t \t0.0 \t            0.0")
print(f"Carry Bag : - {carry_bag} \t \t10.00 \t         10.00")
print(f"GST (10%)   \t   \t        {gst:.2f} \t           {gst:.2f}")
print(f"                                      Thank You                                                        ")
print(f"                                       To Visit                                                        ")
print(f"                                       D-Mart                                                        ") 
print("-----------------------------------------------------------------------------------")
     
