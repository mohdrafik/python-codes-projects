from bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance, "Current")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Allows overdraft withdrawals"""
        if (self.get_balance() + self.overdraft_limit) >= amount:
            self.update_balance(self.get_balance() - amount)
            print(f"Withdrew ${amount}. New Balance: ${self.get_balance()}")
        else:
            print("Overdraft limit exceeded!")
