# Games
# Demonstrates module creation

class Player(object):
	"""
	A player for a game
	"""
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

	def __str__(self):
		rep = self.name + ":\t" + str(self.score)
		return rep

def askYesNo(question):
	"""
	Asks a yes or no question
	"""
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

def askNumber(question, low, high):
	"""
	Ask for a number within a range
	"""
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

# Checks to make sure imported correctly
if __name__ == "__main__":
	print("You ran this module directly (and did not 'import' it).")
	input("\n\nPress the enter key to continue.")