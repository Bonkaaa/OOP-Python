class InsufficientFundsException(Exception):
    def __init__(self, *args, balance, amount):
        super().__init__(f"Insufficient funds: balance = {balance}, attempted withdraw = {amount} ")

class InvalidTransactionException(Exception):
    def __init__(self, *args, message = "Invalid transaction"):
        super().__init__(message)