class BowlingGame:
	counter = 0
	def __init__(self):
		pass

	def roll(self,pins):
		self.counter += pins

	def score(self):

		return self.counter