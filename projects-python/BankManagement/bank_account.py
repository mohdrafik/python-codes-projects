# Defines abstract class and basic account functionality
from abc import ABC, abstractmethod
from datetime import datetime

class BankAccount:

    """ 
    This is an abstract class that provides a common structure for all accounts.
    """
    def __init__(self,name:str,age:int,id:int,account_number:str,balance):
        self.name = name
        self.age = age
        self.id = id
        assert len(account_number) == 5,"enter the 5 digits account number:"
        self.account_number = account_number
        self.__balance = balance  # encapsulation
        self.transaction = []  # store transaction 

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount < 0:
            print(f"invalid amount:{amount}")

        else:
            self.__balance += amount 
            self.transaction.append(f"{datetime.now()} - DESPOSIT:${amount}")
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")

    def withdraw(self,amount):
        if amount < 0 or self.__balance < amount:
            print(f"invalid amount {amount} or insufficient funds:{self.get_balance()}")
         
        else:
            self.__balance -= amount
            self.transaction.append(f" Time and Date: {datetime.now()} - Withdrawn: ${amount}")

    def get_transaction(self):
        return self.transaction
       
        # pass

if __name__ == "__main__":

    bc1 = BankAccount("Ariana",25,125,'00010',100)
    bc1.deposit(1000)
    print(f" {bc1.get_transaction()}")
    bc1.withdraw(200)
    print(f" {bc1.get_transaction()}")





