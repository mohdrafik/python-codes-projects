# Runs the program (entry point)
from savings_account import SavingsAccount
from current_account import CurrentAccount

# Create accounts
alice_savings = SavingsAccount("Alice",51,123,'12345',5000,5)
bob_current = CurrentAccount("Bob",25,321, '30001',3000, 1000)

# Transactions
alice_savings.deposit(1000)
alice_savings.apply_interest()
alice_savings.withdraw(2000)

bob_current.deposit(500)
bob_current.withdraw(4000)
bob_current.withdraw(6000)

# Display Transactions
print("\nAlice's Transactions:")
print(alice_savings.get_transaction())

print("\nBob's Transactions:")
print(bob_current.get_transaction())
