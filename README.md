# Blackjack game
Simple game of blackjack, written in python
Game allows for 1-7 human players and automatically handles the dealer.

Files contained in this project:
cards.py
games.py
blackjack.py


## Cards
The cards.py file is a module written to contain useful classes for card games, specifically cards, hands, and decks. Additional functionality allows the cards to be face up or face down.

## Games
The games.py file contains a player class, assigning a name and a score for a player and has methods allowing the user to input numbers or answer yes/no questions.

## Blackjack
The blackjack.py file is the densest module in the project. It implements the cards and games modules in operating the game of blackjack. It derives the card, hand, deck, and player classes for their blackjack implementation as well as creating a new class for the operation of the game itself, which asks for players, names, bets, and whether or not to continue. Keeps track of money and automatically removes players that go bankrupt.