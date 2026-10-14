class Card:
    number = '0000 0000 0000 0000'
    valiDate = '01/99'
    holder = 'unknown'

    def __init__(self, number, date, holder ):
        self.holder = holder
        self.valiDate = date
        self.number = number

    def pay(self, amount):
        print("с карты", self.number, "списали", amount)     
