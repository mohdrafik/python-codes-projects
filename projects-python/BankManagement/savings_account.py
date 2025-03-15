# Implements savings account with interest

from bank_account import BankAccount
from datetime import datetime

class SavingsAccount(BankAccount):
    def __init__(self, name, age, id, account_number, balance,interest_rate):
        super().__init__(name, age, id, account_number, balance)
        self.interest_rate = interest_rate

    # pass
    def apply_interest(self):
        interest = (self.get_balance())*(self.interest_rate/100) 
        self.deposit(interest)
        print(f"Applied {self.interest_rate}% interest. New Balance: ${self.get_balance()}")

    # def withdraw(self,amount):
    #     if amount < 0 or self.__balance < amount:
    #         print(f"invalid amount {amount} or insufficient funds:{self.get_balance()}")
         
    #     else:
    #         self.__balance -= amount
    #         self.transaction.append(f" Time and Date: {datetime.now()} - Withdrawn: ${amount}")
    def withdraw(self,amount):
        return super().withdraw(amount)







