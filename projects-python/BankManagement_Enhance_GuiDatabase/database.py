import sqlite3

# Create or connect to the database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_number TEXT PRIMARY KEY,
    account_holder TEXT,
    balance REAL,
    account_type TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT,
    transaction_type TEXT,
    amount REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
)
""")

conn.commit()
conn.close()
