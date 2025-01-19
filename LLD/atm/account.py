class Account():
    def __init__(self, account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def getaccountnumber(self):
        return self.account_number

    def getbalance(self):
        return self.balance

    def credit(self,amount):
        self.balance=self.balance+amount

    def debit(self,amount):
        self.balance=self.balance-amount