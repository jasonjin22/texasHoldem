import card

def compare(A, B):
	pass

def sameSuit(A):
	sr = sorted(A, key = lambda kv: kv.suit)
	SuitDic = {}
	for i in sr:
		if i.suit in SuitDic:
			SuitDic[i.suit] += 1
		else:
			SuitDic[i.suit] = 1
	# print(SuitDic)
	if len(SuitDic) == 1:
		sr = sorted(A, key = lambda kv: kv.rank)
		return (True, sr[4].rank)
	else:
		return False
def isStraight(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	currentRank = sr[0].rank
	for card in sr:
		if card == sr[0]:
			continue
		else:
			if (card.rank - currentRank != 1):
				return False
			currentRank = card.rank
	return (True, currentRank)

def isFour(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	result = sr[0].rank == sr[1].rank == sr[2].rank == sr[3].rank \
	or sr[1].rank == sr[2].rank == sr[3].rank == sr[4].rank
	if result:
		four = sr[2]
		if sr[0] == four:
			one = sr[4]
		else:
			one = sr[0]
		return (True, four.rank, one.rank)
	else:
		return False

def isGourd(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	GourdDic = {}
	for i in sr:
		if i.rank in GourdDic:
			GourdDic[i.rank] += 1
		else:
			GourdDic[i.rank] = 1
	if len(GourdDic) == 2:
		for i in GourdDic:
			if GourdDic[i] == 2:
				two = i
			elif GourdDic[i] == 3:
				three = i
			else:
				return False
		return (True, three, two)
	else:
		return False


if __name__ == '__main__':
	A = [card.Card(1, 2), card.Card(2, 9),card.Card(1, 9),card.Card(1, 9),card.Card(1, 9)]
	straight = [card.Card(1, 2), card.Card(2, 3),card.Card(1, 4),card.Card(0, 5),card.Card(1, 6)]
	gourd = [card.Card(1, 2), card.Card(2, 12),card.Card(1, 12),card.Card(0, 2),card.Card(1, 12)]
	thesuit = [card.Card(1, 2), card.Card(1, 12),card.Card(1, 12),card.Card(1, 2),card.Card(1, 12)]
	# print(isStraight(straight))
	# print(isFour(A))
	# print(isGourd(gourd))
	print(sameSuit(thesuit))