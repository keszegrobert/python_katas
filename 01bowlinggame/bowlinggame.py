class BowlingGame:
	rolls = None
	def __init__(self):
		self.rolls = []

	def roll(self,pins):
		self.rolls.append(pins)

	def getBonusForSpare(self,frame):
		return self.rolls[frame+2]

	def getBonusForStrike(self,frame):
		return self.rolls[frame+1] + self.rolls[frame+2]

	def isSpare(self,frame):
		return self.rolls[frame] + self.rolls[frame+1] == 10

	def isStrike(self,frame):
		return self.rolls[frame] == 10

	def scoreForSpare(self,frame):
		return self.rolls[frame] + self.rolls[frame+1]

	def score(self):
		counter = 0
		frameIndex = 0
		for i in range(0,10):
			if self.isStrike(frameIndex):
				counter += 10 + self.getBonusForStrike(frameIndex)
				frameIndex += 1
			elif self.isSpare(frameIndex):
				counter += 10 + self.getBonusForSpare(frameIndex);
				frameIndex += 2
			else:
				counter += self.scoreForSpare(frameIndex)
				frameIndex += 2
		return counter
