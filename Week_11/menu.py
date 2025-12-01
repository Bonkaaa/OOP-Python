from .bank_account import BankAccount
from .notification_services import NotificationService

def main():
    accounts = {}
    notifier = NotificationService()

    def create_account():
        account_id = input("Enter account ID: ")
        account_holder = input("Enter account holder name: ").strip()
        if not account_holder:
            print("Account holder name cannot be empty.")
            return
        balance = float(input("Enter initial balance: "))

        account = BankAccount(account_id, account_holder, balance)
        account._on_transaction_success += notifier.send_transaction_success
        account._on_low_balance += notifier.send_low_balance_alert

        accounts[account_id] = account
        print(f"Account created: {account}")

    def choose_account():
        if not accounts:
            print("No accounts available. Please create an account first.")
            return None
        try:
            account_id = input("Enter account ID: ")
        except ValueError:
            print("Invalid input. Please enter a valid account ID.")
            return None
        account = accounts.get(account_id)
        if not account:
            print("Account not found.")
            return None
        return account
    
    def deposit_to_account():
        account = choose_account()
        if not account:
            return
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print(f"Deposited {amount}. New balance: {account.balance}")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
        except Exception as e:
            print(f"Error: {e}")

    def withdraw_from_account():
        account = choose_account()
        if not account:
            return
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
            print(f"Withdrew {amount}. New balance: {account.balance}")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
        except Exception as e:
            print(f"Error: {e}")

    def view_balance():
        account = choose_account()
        if not account:
            print(f"Account not found.")
            return
        print(f"Account balance: {account.balance}")

    def list_accounts():
        if not accounts:
            print("No accounts available.")
            return
        print("Accounts:")
        for account in accounts.values():
            print(" ", account)

    actions = {
        "1": ("Create Account", create_account),
        "2": ("Deposit", deposit_to_account),
        "3": ("Withdraw", withdraw_from_account),
        "4": ("View Balance", view_balance),
        "5": ("List Accounts", list_accounts),
        "6": ("Exit", None)
    }

    while True:
        print("\nMenu:")
        for key, (desc, _) in actions.items():
            print(f"{key}. {desc}")
        choice = input("Choose an action: ").strip()

        action = actions.get(choice)
        if not action:
            print("Invalid choice. Please try again.")
            continue
        if choice == "6":
            print("Exiting...")
            break

        _, func = action
        func()

if __name__ == "__main__":
    main()
