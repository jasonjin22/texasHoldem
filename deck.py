import card
import random

class Deck(object):
	def __init__(self):
		cardList = []
		for i in range(4):
			for j in range(2, 15):
				cardList.append(card.Card(i, j))
		self.cards = cardList
	def pop(self):
		index = random.randint(0, len(self.cards)-1)
		return self.cards.pop(index)

