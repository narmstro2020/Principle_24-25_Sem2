'''
Create a BankAccount class with:
Instance method: deposit(amount) to add money.
Instance method: withdraw(amount) to subtract money.
Class method: display_bank_info() to show the bank name and total number of accounts.
'''

class BankAccount:
    bank_name = "Fred's Bank"
    num_accounts = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.num_accounts += 1

    def deposit(self, amount):
        #TODO: add amount to self.balance using +=
        pass  # TODO: remove this when done.

    def withdraw(self, amount):
        #TODO: subtract amount from self.balance using the appropriate operator.
        pass  # TODO: remove this when done.

    @classmethod
    def display_bank_info(cls):
        #TODO: print out in a nice format "Bank Name: <insert name here>, Number of Account: <insert num_accounts here>:
        #HINT: use f strings and the {} and cls.
        pass #TODO: remove this when done.

bank_account_1 = BankAccount("Fred", 100)
bank_account_2 = BankAccount("Susie", 200)
bank_account_3 = BankAccount("Billie", 300)
BankAccount.display_bank_info()

