from users import User
from bank import Bank
class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        user = self.bank.create_user()
        account = user.create_account(name, email, address, account_type)
        return account

    def delete_account(self, user, account_number):
        for account in user.accounts:
            if account.account_number == account_number:
                user.accounts.remove(account)
                return f"Account {account_number} deleted successfully."
        return "Account not found."

    def get_all_accounts(self):
        return self.bank.get_all_accounts()

    def total_balance(self):
        return self.bank.total_balance()

    def total_loan_amount(self):
        return self.bank.total_loan_amount()

    def loan_feature(self, status):
        pass
