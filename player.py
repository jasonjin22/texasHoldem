class Player(object):
	def __init__(self, playerid, name, money):
		self.id = playerid
		self.name = name
		self.money = money
		self.playerCard = []
	def __str__(self):
		return "player {}".format(self.id)
	def getCard(self, card):
		self.playerCard.append(card)
	def incomeMoney(self, amount):
		if amount < 0:
			raise ValueError("the amount should be positive")
		self.money += amount
	def outcomeMoney(self, amount):
		if amount < 0:
			raise ValueError("the amount should be positive")
		if amount > self.money:
			raise ValueError("Player does not have enough money")
		self.money -= amount
	def decisionR1(self, currentBet):
		dec = raw_input(str(self)+" enter your input: (0 or >= {})".format(currentBet))
		dec = eval(dec)
		return dec
	def decisionR2(self, currentBet, publicCards, isSB):
		if (isSB):
			print("you are SB and you can pass")
			dec = raw_input(str(self)+" enter your input: (0 or >= {})".format(currentBet))
			dec = eval(dec)
			return dec
		else:
			print("you are not SB, you can either drop or bet some money")
			dec = raw_input(str(self)+" enter your input: (0 or >= {})".format(currentBet))
			dec = eval(dec)
			return dec