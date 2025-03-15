# Tracks deposit/withdrawal transactions

class Transaction:
    def __init__(self,amount,transaction_type,timestamp):
        self.amount = amount 
        self.transaction_type = transaction_type
        self.timestamp = timestamp

        # pass