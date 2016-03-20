class BowlingGame:
	score_table = None
	def __init__(self):
		self.score_table = []

	def roll(self,pins):
		self.score_table.append(pins)

	def score(self):
		counter = 0
		for i in range(0,20):
			counter += self.score_table[i]
		return counter