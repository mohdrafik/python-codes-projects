from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance, "Savings")
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Applies interest to balance"""
        new_balance = self.get_balance() * (1 + self.interest_rate / 100)
        self.update_balance(new_balance)
        print(f"Interest Applied! New Balance: ${new_balance}")

    def withdraw(self, amount):
        """Withdraw money with restrictions"""
        if self.get_balance() >= amount:
            self.update_balance(self.get_balance() - amount)
            print(f"Withdrew ${amount}. New Balance: ${self.get_balance()}")
        else:
            print("Insufficient funds!")
