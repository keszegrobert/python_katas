class BowlingGame:
	rolls = None
	def __init__(self):
		self.rolls = []

	def roll(self,pins):
		self.rolls.append(pins)

	def getBonusForSpare(self,frame):
		return self.rolls[2*frame+2]

	def isSpare(self,frame):
		return self.rolls[2*frame] + self.rolls[2*frame+1] == 10

	def scoreForSpare(self,frame):
		return self.rolls[2*frame] + self.rolls[2*frame+1]

	def score(self):
		counter = 0

		for i in range(0,10):
			if self.isSpare(i):
				counter += 10 + self.getBonusForSpare(i);
			else:
				counter += self.scoreForSpare(i)
		return counter