from .exception import InsufficientFundsException, InvalidTransactionException
from .constant import LOW_BALANCE_THRESHOLD
from typing import Callable, List
from .event import Event

TransactionHandler = Callable[["BankAccount", float], None]

class BankAccount:
    def __init__(self, account_id, account_holder, balance=0):
        self.account_id = account_id
        self.account_holder = account_holder
        self.balance = balance

        self._on_transaction_success = Event()
        self._on_low_balance = Event()
    
    def withdraw(self, amount):
        if amount < 0:
            raise InvalidTransactionException("Withdraw amount must be positive")
        elif amount > self.balance:
            raise InsufficientFundsException()
        
        self.balance -= amount

        self._on_transaction_success(self, -amount)

        if self.balance < LOW_BALANCE_THRESHOLD:
            self._on_low_balance(self)
            

    def deposit(self, amount):
        if amount < 0:
            raise InvalidTransactionException("Deposit amount must be positive")
        self.balance += amount

        # Call success event
        self._on_transaction_success(self, amount)

        if self.balance < LOW_BALANCE_THRESHOLD:
            self._on_low_balance(self)

    def __str__(self):
        return f"[{self.account_id}] {self.account_holder}: {self.balance}"

        


            

    
        
