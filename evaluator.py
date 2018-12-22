from itertools import combinations
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

def isThree(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	ThreeDic = {}
	haveBig = False
	for i in sr:
		if i.rank in ThreeDic:
			ThreeDic[i.rank] += 1
		else:
			ThreeDic[i.rank] = 1
	if len(ThreeDic) == 3:
		for i in ThreeDic:
			if ThreeDic[i] == 3:
				three = i
			elif ThreeDic[i] == 1:
				if not haveBig:
					big = i
					haveBig = True
				else:
					if i > big:
						small = big
						big = i
					else:
						small = i
			else:
				return False
		return (True, three, big, small)
	else:
		return False

def isTwoPairs(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	TwoPairDic = {}
	pairList = []
	for i in sr:
		if i.rank in TwoPairDic:
			TwoPairDic[i.rank] += 1
		else:
			TwoPairDic[i.rank] = 1
	if len(TwoPairDic) == 3:
		for i in TwoPairDic:
			if TwoPairDic[i] == 2:
				pairList.append(i)
			elif TwoPairDic[i] == 1:
				single = i
			else:
				return False
		return (True, max(pairList), min(pairList), single)
	else:
		return False

def isOnePair(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	OnePairDic = {}
	singleList = []
	for i in sr:
		if i.rank in OnePairDic:
			OnePairDic[i.rank] += 1
		else:
			OnePairDic[i.rank] = 1
	if len(OnePairDic) == 4:
		for i in OnePairDic:
			if OnePairDic[i] == 2:
				pair = i
			elif OnePairDic[i] == 1:
				singleList.append(i)
			else:
				return False
		singleList = sorted(singleList, reverse = True)
		return (True, pair, singleList[0], singleList[1], singleList[2])
	else:
		return False

def isAllSingles(A):
	sr = sorted(A, key = lambda kv: kv.rank)
	SingleDic = {}
	singleList = []
	for i in sr:
		singleList.append(i.rank)
		if i.rank in SingleDic:
			SingleDic[i.rank] += 1
		else:
			SingleDic[i.rank] = 1
	if len(SingleDic) == 5:
		singleList = sorted(singleList, reverse = True)
		return (True, singleList[0], singleList[1], singleList[2], singleList[3], singleList[4])
	else:
		return False

def giveValue(A):
	if (isStraight(A) and sameSuit(A)):
		#tonghuashun
		# (True, sr[4].rank)
		# print("sameSuit && straight")
		return sameSuit(A)[1]*1000000000000000000000000 # rank*10^16; min = 5*10^6
	elif (isFour(A)):
		#sitiao
		# (True, four.rank, one.rank)
		# print("four")
		return isFour(A)[1]*10000000000000000000000 + isFour(A)[2]*100000000000000000000 #four*10^14+one*10^12; min = 1*10^14+2*10^12
	elif (isGourd(A)):
		#hulu
		# (True, three, two)
		# print("gourd")
		return isGourd(A)[1]*1000000000000000000 + isGourd(A)[2]*10000000000000000
	elif (sameSuit(A)):
		#tonghua
		# (True, sr[4].rank)
		# print("sameSuit")
		return sameSuit(A)[1]*10000000000000000
	elif (isStraight(A)):
		#shunzi
		# (True, currentRank)
		# print("straight")
		return isStraight(A)[1]*100000000000000
	elif (isThree(A)):
		#santiao
		# (True, three, big, small)
		# print(isThree(A))
		# print("three")
		return isThree(A)[1]*100000000000000 + isThree(A)[2]*5000000000000 + isThree(A)[3]*250000000000
	elif (isTwoPairs(A)):
		#liangdui
		# (True, max(pairList), min(pairList), single)
		# print("twoPairs")
		return isTwoPairs(A)[1]*1000000000000 + isTwoPairs(A)[2]*50000000000 + isTwoPairs(A)[3]*2500000000
	elif (isOnePair(A)):
		#yidui
		# (True, pair, singleList[0], singleList[1], singleList[2])
		# print("onePair")
		return isOnePair(A)[1]*10000000000 + isOnePair(A)[2]*500000000 + isOnePair(A)[3]*25000000 + isOnePair(A)[4]*1250000
	elif (isAllSingles(A)):
		#danpai
		# (True, singleList[0], singleList[1], singleList[2], singleList[3], singleList[4])
		# print("allsingle")
		tem = isAllSingles(A)
		return tem[1]*100000000 + tem[2]*5000000 + tem[3]*250000 + tem[4]*12500 + tem[5]*625
	else:
		print("should not reach here, some bug happens")
		cards = ""
		for i in A:
			cards += str(i)
			cards += ";"
		print(cards[:-1])

def compare(A, B):
	if (giveValue(A) > giveValue(B)):
		return 1
	elif (giveValue(A) < giveValue(B)):
		return -1
	else:
		return 0

def getMax(two, five):
	print("hand: ")
	hand = ""
	for i in two:
		hand += str(i)
		hand += ";"
	print hand[:-1]
	print("public: ")
	pub = ""
	for i in five:
		pub += str(i)
		pub += ";"
	print pub[:-1]
	whole = two + five
	valueDic = {}
	comb = list(combinations(whole, 5))
	for i in comb:
		valueDic[i] = giveValue(i)
	sd = sorted(valueDic.items(), key = lambda kv: kv[1], reverse = True)
	# print(sd[0][0])
	sr = sorted(sd[0][0], key = lambda kv: kv.rank)
	final = ""
	for i in sr:
		final += str(i)
	print ("final: " + final)
	return sd[0][0]



def judge(A, B, Public):
	maxA = getMax(A, Public)
	maxB = getMax(B, Public)
	# compare(maxA, maxB)
	if compare(maxA, maxB) == 1:
		print("jA")
		return A
	elif compare(maxA, maxB) == -1:
		print("jB")
		return B
	else:
		print("jE")
		return (A, B)
	

if __name__ == '__main__':
	KING = [card.Card(1, 10), card.Card(1, 11),card.Card(1, 12),card.Card(1, 13),card.Card(1, 14)]
	A = [card.Card(1, 2), card.Card(2, 9),card.Card(1, 9),card.Card(1, 9),card.Card(1, 9)]
	straight = [card.Card(1, 2), card.Card(2, 3),card.Card(1, 4),card.Card(0, 5),card.Card(1, 6)]
	gourd = [card.Card(1, 2), card.Card(2, 12),card.Card(1, 12),card.Card(0, 2),card.Card(1, 12)]
	thesuit = [card.Card(1, 2), card.Card(1, 3),card.Card(1, 8),card.Card(1, 5),card.Card(1, 6)]
	three1 = [card.Card(1, 8), card.Card(1, 12),card.Card(4, 12),card.Card(1, 2),card.Card(1, 12)]
	three2 = [card.Card(1, 14), card.Card(1, 11),card.Card(4, 11),card.Card(1, 2),card.Card(1, 11)]
	twoPair = [card.Card(1, 7), card.Card(1, 9),card.Card(2, 12),card.Card(1, 7),card.Card(1, 12)]
	onePair = [card.Card(1, 7), card.Card(1, 7),card.Card(0, 8),card.Card(1, 4),card.Card(1, 13)]
	allsingle = [card.Card(1, 7), card.Card(2, 12),card.Card(1, 8),card.Card(1, 4),card.Card(1, 13)]
	hand = [card.Card(2, 4), card.Card(3, 9)]
	# print(isStraight(straight))
	# print(isFour(A))
	# print(isGourd(gourd))
	# print(isThree(three))
	# print(isTwoPairs(twoPair))
	# print(isOnePair(onePair))
	# print(isAllSingles(allsingle))
	# print(giveValue(three1))
	# print(giveValue(three2))
	valueList = [KING, A, straight, gourd, thesuit, three1, three2, twoPair, onePair, allsingle]
	# for i in valueList:
	# print(getMax(hand, allsingle))

	# cd = card.Card
	# Q = [cd(3, 14), cd(0, 3), cd(1, 6), cd(2, 3), cd(3, 6)]
	# W = [cd(1, 9), cd(2, 12), cd(1, 6), cd(0, 10), cd(3, 6)]
	# compare(Q, W)