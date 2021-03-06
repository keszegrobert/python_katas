from bowlinggame import BowlingGame
from unittest import TestCase

#https://github.com/hontas/bowling-game-kata

class TestBowlingGame(TestCase):

	def setUp(self):
	    self.game = BowlingGame()

	def roll_spare(self):
		self.game.roll(7)
		self.game.roll(3)

	def roll_strike(self):
		self.game.roll(10)

	def roll_many(self,rolls,pins):
		for i in range(0,rolls):
			self.game.roll(pins)		

	def test_guttergame(self):
		self.roll_many(20,0)
		assert self.game.score() == 0

	def test_gameofones(self):
		self.roll_many(20,1)
		assert self.game.score() == 20

	def test_spare(self):
		self.roll_spare()
		self.game.roll(4)
		self.roll_many(17,0)
		assert self.game.score() == 10+4+4

	def test_strike(self):
		self.roll_strike()
		self.game.roll(3)
		self.game.roll(4)
		self.roll_many(16,0)
		assert self.game.score() == 10 + (3+4) + (3+4)

	def test_perfectgame(self):
		self.roll_many(12,10)
		assert self.game.score() == 300

if __name__ == '__main__':
	unittest.main()