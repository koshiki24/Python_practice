'''2. Bank Account Simulation
Problem

Design a banking system using OOP.

Requirements

Each account should contain:

account number
holder name
balance
Functionalities
Deposit money
Withdraw money
Prevent withdrawal if balance insufficient
Display account summary
Maintain bank-wide interest rate as class variable
Add static method to validate minimum balance rule
Concepts Practiced
object state management
static methods
class variables
validations'''

class Bank:
    minimum_balance = 500
    interest_rate = 5
    def __init__(self,acc_no,holder_name,balance):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit_money(self):
        amount = int(input("Enter amount you want to deposit : "))
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
            print(f"Current balance is : {self.__balance}")
        else:
            print("Invalid amount!")

    def withdraw_money(self):
        withdraw = int(input("Enter amount you want to withdraw :"))
        if withdraw <= 0:
            print("Invalid amount!")
        elif Bank.validate_balance(self.__balance - withdraw):
            self.__balance -= withdraw
            print("Money withdrawn successfully!")
            print(f"Remaining amount is : {self.__balance}")

        else:
            print("Insufficient balance")

    def account_summary(self):
        print(f"Account Number : {self.__acc_no}\nHolder Name : {self.__holder_name}\nBalance : {self.__balance}")

    @classmethod
    def interest(cls):
        print(f"Current Intrest rate is : {cls.interest_rate}%")
        
    @staticmethod
    def validate_balance(balance):
        if balance>=Bank.minimum_balance:
            return True
        else:
            return False

b1 = Bank(101,"Koshiki",1000)
b1.deposit_money()
b1.withdraw_money()
b1.account_summary()
Bank.interest()
print(Bank.validate_balance(1000))

