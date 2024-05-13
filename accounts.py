import uuid
class Account:
    def __init__(self, name, email, address, account_type):
        self.account_number = uuid.uuid4().hex[:6].upper() 
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient balance to transfer")
        elif recipient is None:
            print("Recipient account does not exist")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred ${amount} to account {recipient.account_number}")

    def check_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions
