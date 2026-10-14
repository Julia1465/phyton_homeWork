from user import User
from card import Card

Aleks = User("Aleks")

Aleks.sayName()
Aleks.setAge(35)
Aleks.sayAge()

card = Card("4526 4756 2565 8712", "11/28", "Aleks F")

Aleks.addCard(card)
Aleks.getCard().pay(1000)

