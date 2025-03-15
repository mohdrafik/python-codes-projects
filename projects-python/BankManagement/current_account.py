# Implements a CurrentAccount with an overdraft limit.

from bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, name, age, id, account_number, balance,overdraft_limit):
        super().__init__(name, age, id, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if (self.get_balance() + self.overdraft_limit) >= amount:
            return super().withdraw(amount)
            # print(f"Withdrew ${amount}. New Balance: ${self.get_balance()}")
        else:
            print("Overdraft limit exceeded!")
        # return super().withdraw(amount)()
    