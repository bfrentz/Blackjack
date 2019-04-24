# Blackjack
# From 1 to 7 players
# Compete against a computer dealer

import cards, games

class bjCard(cards.Card):
	"""
	A blackjack card with a value
	"""
	ACE_VALUE = 1

	@property
	def value(self):
		if self.isFaceUp:
			v = bjCard.RANKS.index(self.rank) + 1  		# ranks are in a list where index + 1 = rank
			if v > 10:
				v = 10
		else:
			v = None
		return v


class bjDeck(cards.Deck):
	"""
	A blackjack deck
	"""
	def populate(self):
		for suit in bjCard.SUITS:
			for rank in bjCard.RANKS:
				self.cards.append(bjCard(rank, suit))


class bjHand(cards.Hand):
	"""
	A blackjack hand
	"""
	def __init__(self, name):
		super(bjHand, self).__init__()
		self.name = name

	def __str__(self):
		rep = self.name + ":\t" + super(bjHand, self).__str__()
		if self.total:
			rep += "(" + str(self.total) + ")"
		return rep

	@property
	def total(self):
		# if a card in the hand has a value of None, then the total is None
		for card in self.cards:
			if not card.value:
				return None

		# add up the card values, treating the ace as 1
		t = 0
		for card in self.cards:
			t += card.value

		# determine if the hand contains an Ace
		containsAce = False
		for card in self.cards:
			if card.value == bjCard.ACE_VALUE:
				containsAce = True

		# if the hand contains an Ace and total is low enough, treat ace as 11
		if containsAce and t <= 11:
			# add only 10 since we already counted 1 for the ace
			t += 10

		return t

	def isBusted(self):
		return self.total > 21


class bjPlayer(bjHand):
	"""
	A blackjack player
	"""
	def __init__(self, name, money):
		super(bjPlayer, self).__init__()
		self.name = name
		self.money = money

	def isHitting(self):
		response = games.askYesNo("\n" + self.name + ", do you want a hit? (Y/N): ")
		return response == "y"

	def bust(self):
		print(self.name, "busts.")
		self.lose()

	def lose(self, bet):
		print(self.name, "loses $", self.money, ".")
		self.money -= bet

	def win(self, bet):
		print(self.name, "wins $", self.money, ".")
		self.money += bet

	def push(self):
		print(self.name, "pushes.")

	def isBroke(self):
		return self.money <= 0

	def maxBet(self):
		return self.money


class bjDealer(bjHand):
	"""
	A blackjack dealer
	"""
	def isHitting(self):
		return self.total < 17

	def bust(self):
		print(self.name, "busts.")

	def flipFirstCard(self):
		firstCard = self.cards[0]
		firstCard.flip()


class bjGame(object):
	"""
	A blackjack game
	"""
	def __init__(self, names, money):
		self.players = []
		for name in names:
			player = bjPlayer(name, money)
			self.players.append(player)

		self.dealer = bjDealer("Dealer")

		self.deck = bjDeck()
		self.deck.populate()
		self.deck.shuffle()

	@property
	def stillPlaying(self):
		sp = []
		for player in self.players:
			if not player.isBusted():
				sp.append(player)
		return sp

	def __additionalCards(self, player):
		while not player.isBusted() and player.isHitting():
			self.deck.deal([player])
			print(player)
			if player.isBusted():
				player.bust()			# both player and dealer have bust method so this is great

	def play(self):
		# deal two cards to everyone initially
		self.deck.deal(self.players + [self.dealer], perHand = 2)
		self.dealer.flipFirstCard()  	# hide the dealer's first card
		for player in self.players:
			print(player)
		print(self.dealer)

		# deal additional cards to players
		for player in self.players:
			self.__additionalCards(player)

		self.dealer.flipFirstCard() 	# reveal the dealers first card

		if not self.stillPlaying:
			# all busted, show the dealers hand
			print(self.dealer)
		else:
			# deal additional cards to dealer
			print(self.dealer)
			self.__additionalCards(self.dealer)

			if self.dealer.isBusted():
				# everyone still playing wins
				for player in self.stillPlaying:
					player.win()
			else:
				# compare the player to the dealer
				for player in self.stillPlaying:
					if player.total > self.dealer.total:
						player.win()
					elif player.total < self.dealer.total:
						player.lose()
					else:
						player.push()

		#remove everyone's cards
		for player in self.players:
			player.clear()
		self.dealer.clear()

	def reshuffle(self):
		self.deck.clear()
		self.deck.populate()
		self.deck.shuffle()


# main
def main():
	print("\n\t\tWelcome to the Blackjack table!\n")

	names = []
	money = []
	number = games.askNumber("How many people are playing? (1 - 7): ", low = 1, high = 8)
	for i in range(number):
		name = input("Enter player name: ")
		cash = input("How much money do they have? ")
		names.append(name)
		money.append(cash)

	print()

	# initialize game
	game = bjGame(names, money)

	again = None
	while again != "n":
		game.play()
		again = games.askYesNo("\nDo you want to play again? (y/n): ")
		if again == "y":
			game.reshuffle()
			print("\nShuffling the deck.\n\n")

	print("\nThanks for playing! We hope you'll visit the virtual casino again soon!\n")


# program
main()



