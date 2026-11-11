# '''9. ATM Machine Simulation
# Problem

# Design ATM software.

# Requirements

# Each account should have:

# account number
# PIN
# balance
# Functionalities
# Login verification
# Withdraw
# Deposit
# Change PIN
# Mini statement
# Additional Challenge

# Lock account after 3 wrong PIN attempts.

# Concepts Practiced
# encapsulation mindset
# validations
# object state'''

class ATM:
    def __init__(self,account_no,PIN,balance):
        self.__account_no = account_no
        self.__PIN = PIN
        self.__balance = balance
        self.__attempts = 0
        self.__is_locked = False
        self.__transactions = []
        self.__is_logged_in = False

    def login(self):
        if self.__is_locked:
            print("Account is locked")
            return False

        while self.__attempts < 3:
            pin = input("Enter 4 digit pin :")

            if pin == self.__PIN:
                print("Login successfully!")
                self.__is_logged_in = True
                self.__attempts = 0
                return True

            else:
                self.__attempts+=1
                remaining = 3 - self.__attempts

                if remaining > 0:
                    print("Incorrect pin!")
                    print("Remaining Attempts : ",remaining)
                else:
                    self.__is_locked = True
                    print("Account is locked after 3 incorrect attempts!")
                    return False

    def withdraw(self):
        if not self.__is_logged_in:
            print("Please login first!")
            return

        amount = int(input("Enter amount you want to withdraw :"))
        if amount <=0:
            print("Invalid amount!")

        elif amount > self.__balance:
            print("Insufficient balance!")

        else:
            self.__balance-=amount
            self.__transactions.append("Withdraw :"+str(amount))
            print("Withdrawal successfully!")
            print("Remaining balance :",self.__balance)

    def deposit(self):
        if not self.__is_logged_in:
            print("Please login first!")
            return

        amount = int(input("Enter amount you want to deposit :"))

        if amount <= 0:
            print("Invalid amount!")

        else:
            self.__balance+=amount
            self.__transactions.append("Deposit :"+str(amount))
            print("Deposit successfully!" \
            "" \
            "")
            print("Updated balance",self.__balance)

    def change_PIN(self):
        if not self.__is_logged_in:
            print("Please log in first")
            return

        old_pin = input("Enter old pin :")

        if old_pin == self.__PIN:
            new_pin = input("Enter your new PIN :")
            confirm_pin = input("Enter your new pin :")

            if new_pin == confirm_pin:
                self.__PIN = new_pin
                print("PIN changed successfully!")

            else:
                print("PIN does not match")

        else:
            print("Incorrect old pin")

    def mini_statement(self):
        if not self.__is_logged_in:
            print("Please login first")
            return

        print("\n----------MINI STATEMENT----------")
        print("Account Number :",self.__account_no)
        print("Current Balance :",self.__balance)
        print("\nTransaction History :")

        if len(self.__transactions) == 0:
            print("No transaction yet!")

        else:
            for transaction in self.__transactions:
                print(transaction)

        print("-------------------------------------")

a1 = ATM("123456789","1234",100000)

if a1.login():
    while True:
        print("\n=====ATM MENU=====")
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Change PIN")
        print("4.Mini Statement")
        print("5.Exit")

        choice = input("Enter your choice :")

        if choice == '1':
            a1.withdraw()

        elif choice == '2':
            a1.deposit()

        elif choice == '3':
            a1.change_PIN()

        elif choice == '4':
            a1.mini_statement()

        elif choice == '5':
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")


