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

	def getScoreForFrame(self,frame):
		if self.isStrike(frame):
			return 10 + self.getBonusForStrike(frame)
		elif self.isSpare(frame):
			return 10 + self.getBonusForSpare(frame);
		else:
			return self.scoreForSpare(frame)

	def score(self):
		counter = 0
		frameIndex = 0
		for i in range(0,10):
			counter += self.getScoreForFrame(frameIndex)
			frameIndex += 1 if self.isStrike(frameIndex) else 2
		return counter
