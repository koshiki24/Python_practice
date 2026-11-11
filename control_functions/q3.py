'''3. ATM Banking Simulator
Beginner–Intermediate
Concepts: Nested conditions, loops, functions
Requirements
•	Verify a PIN.
•	Display balance, deposit, withdrawal, and exit options.
•	Prevent withdrawals exceeding the available balance.
•	Reject invalid amounts.
•	Use separate functions for deposit, withdrawal, and balance enquiry.
Bonus: Allow only three PIN attempts.
'''

'''ATM Banking Simulator
1. Balance Enquiry
2. Deposit
3. Withdraw
4. Exit'''


balance = 5000


def display_balance(balance):
    return balance
def display_deposit(balance):
    deposite = int(input("Enter the amount you want to deposit : "))
    if deposite > 0:
        balance = balance + deposite
        print("Money deposited successully!")
    else:
        print("Insufficient balance!")
    return balance
def display_withdrawal(balance):
    withdraw = int(input("Enter how much amount you want to withdraw :"))
    if withdraw <= 0:
        print("Insufficient amount!")
    elif withdraw > balance:
        print("Insufficient Balance!")
    else:
        balance = balance - withdraw
        print("Money withdrawn successfully!")
    return balance
def check_balance(balance):
    return balance
def check_pin():
    count = 0
    
    while(count<3):
        pin = int(input("Enter four digit pin : "))

        if pin == correct_pin:
            print("PIN verified successfully")
            return True
        else:
            print("Incorrect PIN! Try Again")
            count+=1
    print("Three Attempts failed! Access Denied")
    return False


correct_pin = 1234
if check_pin():
    while True:
        print("\nWelcome to ATM")
        print("1. Balance Enquiry")
        print("2.Deposit")
        print("3. Money Withdrawal")
        print("4. Exit")
        
        choice = int(input("Enter choice :"))
        
        if choice == 1:
            balance = check_balance(balance)
            print(f"Your account balance is : {balance}")

        elif choice == 2:
            balance = display_deposit(balance)

        elif choice == 3:
            balance = display_withdrawal(balance)
        elif choice == 4:
            print("ATM Exited")
            break
        else:
            print("Invalid Choice")


        

    



