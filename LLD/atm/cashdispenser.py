import threading
class CashDispenser():
    def __init__(self, initalamount):
        self.amount=initalamount
        self.lock=threading.Lock() #thread lock allows us to put a locks on a transaction so that another transaction is 
                                   # not allowed concurrently. Note: this has to be an instance variable not a local variable
                                   # as it needs to be shared across threads. if defined locally then every transactions gets its own
                                   # thread which are not shared defeating the purpose of thread locking. This will be defined when we
                                   # first call the cashdispenser class. Now, the first thread is locked when dispense_cash is called.
    def dispense_cash(self, amount):
        with self.lock: # Thread is locked across the cashdispenser class and released automatically at the end of method execution
            if amount > self.cash_available: # at the same time if some other call is made then it is put on hold until the prev lock is released
                raise ValueError("Insufficient cash in ATM")
            self.cash_available -= amount
            print("Cash dispensed:", amount)
            
