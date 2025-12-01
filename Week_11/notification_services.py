from .bank_account import BankAccount

class NotificationService:
    def send_low_balance_alert(self, sender: BankAccount, balance: float) -> None:
        print(f"Alert: Low balance on account {sender.account_id}. Current balance: {balance}")

    def send_transaction_success(self, sender: BankAccount, amount: float) -> None:
        transaction_type = "Deposit" if amount > 0 else "Withdrawal"
        print(f"Notification: {transaction_type} of {abs(amount)} successful on account {sender.account_id}. New balance: {sender.balance}")