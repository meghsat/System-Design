from account import Account

class BankingService():
    def __init__(self):
        self.accounts={}
    
    def create_account(self, account_number, initial_balance):
        self.accounts[account_number]=Account(account_number, initial_balance)

    def delete_account(self, account_number):
        del self.accounts[account_number]

    def get_account(self, account_number):
        return self.accounts[account_number]
    
    def process_transaction(self, transaction):
        transaction.execute()