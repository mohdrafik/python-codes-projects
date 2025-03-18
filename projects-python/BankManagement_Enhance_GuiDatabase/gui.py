import tkinter as tk
from savings_account import SavingsAccount
from current_account import CurrentAccount
# from bank import Bank

def create_account():
    """Creates a new Savings or Current account"""
    account_number = entry_acc_number.get()
    account_holder = entry_acc_holder.get()
    balance = float(entry_balance.get())

    if account_type.get() == "Savings":
        interest_rate = float(entry_interest.get())
        account = SavingsAccount(account_number, account_holder, balance, interest_rate)
    else:
        overdraft_limit = float(entry_overdraft.get())
        account = CurrentAccount(account_number, account_holder, balance, overdraft_limit)

    # Bank.add_account(account)
    status_label.config(text="Account Created Successfully!")

def deposit_money():
    """Handles deposits to an account"""
    account_number = entry_acc_number.get()
    amount = float(entry_amount.get())

    account = SavingsAccount(account_number, "", 0, 0)  # Creating a temporary object
    account.deposit(amount)
    status_label.config(text="Deposit Successful!")

# ✅ Creating GUI Window
window = tk.Tk()
window.title("Bank Management System")

# Account Number
tk.Label(window, text="Account Number:").pack()
entry_acc_number = tk.Entry(window)
entry_acc_number.pack()

# Account Holder Name
tk.Label(window, text="Account Holder:").pack()
entry_acc_holder = tk.Entry(window)
entry_acc_holder.pack()

# Balance
tk.Label(window, text="Initial Balance:").pack()
entry_balance = tk.Entry(window)
entry_balance.pack()

# Account Type Selection
account_type = tk.StringVar(value="Savings")
tk.Radiobutton(window, text="Savings", variable=account_type, value="Savings").pack()
tk.Radiobutton(window, text="Current", variable=account_type, value="Current").pack()

# Additional Field (Interest Rate or Overdraft Limit)
tk.Label(window, text="Interest Rate (Savings) / Overdraft Limit (Current):").pack()
entry_interest = tk.Entry(window)  # Used for interest rate (Savings)
entry_overdraft = tk.Entry(window)  # Used for overdraft (Current)
entry_interest.pack()
entry_overdraft.pack()

# Buttons
tk.Button(window, text="Create Account", command=create_account).pack()
tk.Button(window, text="Deposit", command=deposit_money).pack()

# Status Label
status_label = tk.Label(window, text="")
status_label.pack()

# ✅ Run the GUI Application
window.mainloop()

# import tkinter as tk
# from savings_account import SavingsAccount
# from current_account import CurrentAccount

# def create_account():
#     account_number = entry_acc_number.get()
#     account_holder = entry_acc_holder.get()
#     balance = float(entry_balance.get())

#     if account_type.get() == "Savings":
#         interest_rate = float(entry_interest.get())
#         account = SavingsAccount(account_number, account_holder, balance, interest_rate)
#     else:
#         overdraft_limit = float(entry_overdraft.get())
#         account = CurrentAccount(account_number, account_holder, balance, overdraft_limit)

#     status_label.config(text="Account Created Successfully!")

# def deposit_money():
#     account_number = entry_acc_number.get()
#     amount = float(entry_amount.get())

#     account = SavingsAccount(account_number, "", 0, 0)  # Dummy object
#     account.deposit(amount)
#     status_label.config(text="Deposit Successful!")

# # Creating GUI Window
# window = tk.Tk()
# window.title("Bank Management System")

# tk.Label(window, text="Account Number:").pack()
# entry_acc_number = tk.Entry(window)
# entry_acc_number.pack()

# tk.Label(window, text="Account Holder:").pack()
# entry_acc_holder = tk.Entry(window)
# entry_acc_holder.pack()

# tk.Label(window, text="Balance:").pack()
# entry_balance = tk.Entry(window)
# entry_balance.pack()

# account_type = tk.StringVar(value="Savings")
# tk.Radiobutton(window, text="Savings", variable=account_type, value="Savings").pack()
# tk.Radiobutton(window, text="Current", variable=account_type, value="Current").pack()

# entry_interest = tk.Entry(window)
# entry_overdraft = tk.Entry(window)

# tk.Button(window, text="Create Account", command=create_account).pack()
# tk.Button(window, text="Deposit", command=deposit_money).pack()

# status_label = tk.Label(window, text="")
# status_label.pack()

# window.mainloop()
