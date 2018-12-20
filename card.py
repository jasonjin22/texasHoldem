#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Card(object):
	RANKS = {
		2: "2",
		3: "3",
		4: "4",
		5: "5",
		6: "6",
		7: "7",
		8: "8",
		9: "9",
		10: "10",
		11: "J",
		12: "Q",
		13: "K",
		14: "A",
	}
	SUITS = {
		3: u"\u2665",  # Hearts
		2: u"\u2666",  # Diamonds
		1: u"\u2663",  # Clubs
		0: u"\u2660",  # Spades
	}
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return Card.SUITS[self.suit].encode("utf-8")+Card.RANKS[self.rank].encode("utf-8")

# if __name__ == "__main__":
# 	card = Card(1, 5)
# 	print(card)