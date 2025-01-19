import threading
from withdrawl_transaction import WithdrawlTransaction
from deposit_transaction import DepositTransaction

class ATM():
    def __init__(self, banking_service, cash_dispenser):
        self.banking_service=banking_service
        self.cash_dispenser=cash_dispenser
        self.transactions=0
        self.lock_transaction=threading.lock


    def check_balance(self, account_number):
        balance=self.banking_service.get_account(account_number).get_balance()
        return balance
    
    def withdraw_cash(self, account_number, amount):
        account=self.banking_service.get_account(account_number)
        transaction=WithdrawlTransaction(self.new_transaction_id, account, amount)
        self.banking_service.process_transaction(transaction)
        self.cash_dispenser.dispense_cash(amount)
    
    def deposit_cash(self, account_number, amount):
        account=self.banking_service.get_account(account_number)
        transaction=DepositTransaction(self.new_transaction_id,account, amount)
        self.banking_service.process_transaction(transaction)
        

    def new_transaction_id(self):
        self.transactions+=1
        return self.transactions
        
        