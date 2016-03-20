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
