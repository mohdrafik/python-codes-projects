

class BankAccount:
    """
    Create a class BankAccount that has:
    A class variable bank_name set to "ABC Bank".
    An __init__() method that initializes:
    account_number
    account_holder
    balance (default to 0)
    A class method change_bank_name(cls, new_name) to update the bank's name.
    A static method validate_amount(amount) to check if the amount is positive.
    An deposit(amount) method to add money (only if the amount is valid).
    A withdraw(amount) method to withdraw money (only if the amount is valid and does not exceed balance).
    A display_info() method to print account details.
    """
    bank_name = "UniCreditBank"

    def __init__(self,account_number:int,account_holder:str,balance:float):
        assert account_number >=0,'account can\'t be a negative number:' 
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    @classmethod
    def update_bank_name(cls,new_name):
        cls.bank_name = new_name
        print(f"name is updated to {new_name}") 

    # @staticmethod
    # def validate_amount(amount):
    #     if amount>=0:
    #         # print(f"amount is validated")
    #         return True
    #     else:
    #         # print(f"amount is not valid")
    #         return False
    
    @staticmethod
    def validate_amount(amount):
        return amount >= 0  # No need to print messages
    
    # def deposit(self,amount):
    #     # self.amount = amount  # unnecessary

    #     if self.validate_amount(amount):
    #         self.balance = self.balance + amount

    #     else:
    #         print(f"enter valid amount")
    #     #     self.balance = self.balance
    #     # self.amount = amount

    # """
    def deposit(self, amount):
        if not self.validate_amount(amount):
            print("Enter a valid deposit amount!")
            return
        self.balance += amount
    # """


    # def withdraw(self,amount):
    #     # self.amount = amount
    #     if self.validate_amount(amount):
    #         if self.balance >= amount:
    #             self.balance = self.balance - amount
    #         else:
    #             print(f"Insufficient Balance")
    #     else:
    #         print(f"enter valid amount")
    #         # self.balance = self.balance
    
    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Enter a valid withdrawal amount!")
            return False
        if self.balance < amount:
            print("Insufficient balance!")
            return False
        self.balance -= amount
        return True
  
    def display_info(self):
        print(
            f"account number --> {self.account_number}\n bank name:--> {BankAccount.bank_name} \n account holder name :--> {self.account_holder}\n balance:--> {self.balance} \n")


ac1 = BankAccount(123,"John Doe",1000)
ac1.deposit(1500)
ac1.withdraw(3000)
ac1.display_info()
BankAccount.update_bank_name("posteItaliane")
ac1.display_info()










