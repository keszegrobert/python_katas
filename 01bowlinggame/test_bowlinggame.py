from bowlinggame import BowlingGame
from unittest import TestCase

#https://github.com/hontas/bowling-game-kata

class TestBowlingGame(TestCase):
	game = None

	def setUp(self):
	    self.game = BowlingGame()

	def tearDown(self):
	    pass

	def test_guttergame(self):
		for i in range(0,20):
			self.game.roll(0)
		assert self.game.score() == 0

	def test_gameofones(self):
		for i in range(0,20):
			self.game.roll(1)
		assert self.game.score() == 20

	def test_spare(self):
		self.game.roll(7)
		self.game.roll(3)
		self.game.roll(4)
		for i in range(0,17):
			self.game.roll(0)
		assert self.game.score() == 10+4+4

	
