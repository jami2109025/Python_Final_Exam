from users import User

class Bank:
    def __init__(self,name):
        self.users = []
        self.name = name

    def create_user(self):
        user = User()
        self.users.append(user)
        return user

    def delete_user(self, user):
        self.users.remove(user)

    def get_all_accounts(self):
        all_accounts = []
        for user in self.users:
            all_accounts.extend(user.accounts)
        return all_accounts

    def total_balance(self):
        total_balance = sum(account.balance for account in self.get_all_accounts())
        return total_balance

    def total_loan_amount(self):
        total_loan_amount = sum(user.loan_taken for user in self.users)
        return total_loan_amount

