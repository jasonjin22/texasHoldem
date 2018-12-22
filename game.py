import deck
import player
import evaluator

initMoney = 1000
BBAmount = 10
SBAmount = 5
finished = False

class Game(object):
	def __init__(self, playerList, banker, playerNum, SB, BB):
		self.deck = deck.Deck()
		self.publicCards = []
		self.totalBet = 0
		self.banker = banker
		self.playerList = playerList
		self.playerNum = playerNum
		self.SB = SB
		self.BB = BB
		self.currentBet = BBAmount

	def addPubCard(self, card):
		self.publicCards.append(card)

	def showPubCard(self):
		print("here are the public cards:")
		s = ""
		for card in self.publicCards:
			s = s + str(card) + ","
		s = s[:-1]
		print(s)
		print(str(self.playerNum)+" players remain in the game")

	def addBet(self, bet):
		self.totalBet += bet
		print("the totalBet: "+str(self.totalBet))

	def dropPlayer(self, player):
		print("dropPlayer")			
		self.playerList.remove(player)
		self.playerNum -= 1
		if player == self.SB:
			self.SB = self.playerList[0]
		if (self.playerNum == 1):
			self.finish(self.playerList[0])

	def round0(self):
		self.addBet(BBAmount)
		self.BB.outcomeMoney(BBAmount)
		self.addBet(SBAmount)
		self.SB.outcomeMoney(SBAmount)

		for player in self.playerList:
			for i in range(2):
				player.getCard(self.deck.pop())
		for player in self.playerList:
			print(str(player)+"-----------------------")
			for i in range(2):
				print(player.playerCard[i])

	def round1(self):
		for player in self.playerList:
			if player == self.SB or player == self.BB:
				continue
			else:
				bet = player.decisionR1(self.currentBet)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)

	def round2(self):
		self.currentBet = 0
		for i in range(3):
				self.addPubCard(self.deck.pop())
		self.showPubCard()
		for player in self.playerList:
			if player == self.SB:
				bet = player.decisionR2(self.currentBet, self.publicCards, True)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)
			else:
				bet = player.decisionR2(self.currentBet, self.publicCards, False)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)

	def round3(self):
		print("\nround3!!!")
		self.currentBet = 0
		for i in range(1):
				self.addPubCard(self.deck.pop())
		self.showPubCard()
		for player in self.playerList:
			if player == self.SB:
				bet = player.decisionR2(self.currentBet, self.publicCards, True)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)
			else:
				bet = player.decisionR2(self.currentBet, self.publicCards, False)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)
	def round4(self):
		print("\nround4!!!!!")
		self.currentBet = 0
		for i in range(1):
				self.addPubCard(self.deck.pop())
		self.showPubCard()
		for player in self.playerList:
			if player == self.SB:
				bet = player.decisionR2(self.currentBet, self.publicCards, True)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)
			else:
				bet = player.decisionR2(self.currentBet, self.publicCards, False)
				if (bet >= self.currentBet):
					self.currentBet = bet
					self.addBet(bet)
					player.outcomeMoney(bet)
				else:
					print(bet, self.currentBet)
					self.dropPlayer(player)

	def finish(self, winner):
		global finished
		print("\n"+str(winner)+" has winned "+str(self.totalBet)+" money")
		winner.incomeMoney(self.totalBet)
		finished = True

	def evaluate(self):
		# self.showPubCard()
		A = self.playerList[0].playerCard
		B = self.playerList[1].playerCard
		P = self.publicCards
		# print(str(self.playerList[0])+"'s cards: ")
		# A_cards = ""
		# for i in A:
		# 	A_cards+=str(i)
		# print(A_cards)
		# print(str(self.playerList[1])+"'s cards: ")
		# A_cards = ""
		# for i in B:
		# 	A_cards+=str(i)
		# print(A_cards)
		winner = evaluator.judge(A, B, P)
		if type(winner) != tuple:
			if winner == A:
				print (str(self.playerList[0])+" wins")
			else:
				print (str(self.playerList[1])+" wins")
		else:
			print("equal")



if __name__ == '__main__':
	p1 = player.Player(0, "P1", initMoney)
	p2 = player.Player(1, "P2", initMoney)
	# p3 = player.Player(2, "P3", initMoney)
	game = Game([p1, p2], p1, 2, p1, p2)
	game.round0()
	if not finished: game.round1()
	if not finished: game.round2()
	if not finished: game.round3()
	if not finished: game.round4()
	if not finished: game.evaluate()
	print(game.totalBet)
