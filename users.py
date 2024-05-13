from accounts import Account
class User:
    def __init__(self):
        self.accounts = []
        self.loan_taken = 0

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        return account

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            return f"You have taken a loan of ${amount}"
        else:
            return "You can't take more than two loans."