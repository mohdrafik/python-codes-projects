import sqlite3
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, account_holder, balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.__balance = balance  # Encapsulation

        # Save to database
        self.save_account()

    def save_account(self):
        """Save the account details in the database."""
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO accounts VALUES (?, ?, ?, ?)", 
                       (self.account_number, self.account_holder, self.__balance, self.account_type))
        conn.commit()
        conn.close()

    def get_balance(self):
        """Retrieve balance from database"""
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = cursor.fetchone()[0]
        conn.close()
        return balance

    def update_balance(self, new_balance):
        """Update balance in the database"""
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", 
                       (new_balance, self.account_number))
        conn.commit()
        conn.close()

    def deposit(self, amount):
        """Deposit money and update transaction history"""
        new_balance = self.get_balance() + amount
        self.update_balance(new_balance)

        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, 'Deposit', ?)", 
                       (self.account_number, amount))
        conn.commit()
        conn.close()

        print(f"Deposited ${amount}. New Balance: ${new_balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass
