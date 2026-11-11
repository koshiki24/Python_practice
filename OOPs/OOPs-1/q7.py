'''Write a Java program to create a class called "Bank" with a collection of accounts and methods to add and remove accounts, and to deposit and withdraw money. Also define a class called "Account" to maintain account details of a particular customer.
'''

class Bank:
    def __init__(self,name,contact,account_no,city,balance):
        self.__name = name
        self.__contact = contact
        self.__account_no = account_no
        self.__city = city
        self.__balance = balance
        self.accounts = []

    def add_account(self,account):
        account = {
            "name" : self.__name,
            "contact" : self.__contact,
            "account_no" : self.__account_no,
            "city" : self.__city,
            "balance" : self.__balance
        }
        self.accounts.append(account)
        print("Account added successfully")

    def remove_account(self,account_no):
        for account in self.accounts():
            if account["account_no"] == self.__account_no:
                self.accounts.remove(account)
                print("Account removed successfully")
                return
        print("Account not found")

    def deposite(self,account_no,amount):
        for account in self.accounts:
            if account["account_no"] == self.account_no:
                account["balance"] += amount
                print("Money deposited successfully")

    def withdraw(self,account_no,amount):
        for account in self.accounts:
            if account["account_no"] == self.__account_no:
                if account["balance"] >= amount:
                    account["balance"] -= amount
                    print("Money withdraw successfully")
                else:
                    print("Invalid balance!!")
            else:
                print("Account not found!")

