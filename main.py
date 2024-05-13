from users import User
from accounts import Account
from bank import Bank
from admin import Admin

bank = Bank("Pubali Bank Limited")
def user_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    user = User(name,email,address)

    while True:
        print(f'Welcome {user.name}!!!')
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit!!")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            account_type = input("Enter account type (Savings/Current): ")
            account = user.create_account(account_type)
            print("Account created successfully!")
        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 4:
            account.check_balance()
        elif choice == 5:
            recipient_name = input("Enter recipient name: ")
            amount = float(input("Enter transfer amount: "))
            recipient = user(recipient_name, "", "")
            account.transfer(amount, recipient)
        elif choice == 6:
            break
        else:
            print("Invalid choice!!")
            
            
def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    admin = Admin(name,email,address)

    while True:
        print(f'Welcome {admin.name}!!!')
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See all users account list")
        print("4. Check total available Balance")
        print("5. Check total loan amount")
        print("6. Loan Feature of the bank")
        print("7. Exit!!")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            account_type = input("Enter account type (Savings/Current): ")
            account = admin.create_account(account_type)
            print("Account created successfully!")
            
        elif choice == 2:
            user = input("Enter user name: ")
            account = input("Enter account number: ")
            admin.delete_account(user,account)
            
        elif choice == 3:
            admin.get_all_accounts()
            
        elif choice == 4:
            admin.check_balance()
            
        elif choice == 5:
            admin.total_loan_amount()
        
        elif choice == 6:
            admin.loan_feature()
            
        elif choice == 7:
            break
        else:
            print("Invalid choice!!")
            


while True:
    print(f"*****WELCOME to {bank.name}*****")
    print("1. User Menu")
    print("2. Admin Menu")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid choice!!!!")
