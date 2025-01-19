

class card():
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
    
    def get_card_number(self):
        return self.cardnumber

    def get_pin(self):
        return self.pin