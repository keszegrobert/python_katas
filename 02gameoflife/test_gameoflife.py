from unittest import TestCase
from gameoflife import GameOfLife

class TestGameOfLife(TestCase):
	def setUp(self):
		self.game = GameOfLife()

	def test_if_any_cell_with_less_than_two_neighbours_dies(self):
		next_generation = self.game.evolve([(0,0)])
		self.assertFalse((0,0) in next_generation)
		next_generation = self.game.evolve([(0,0),(1,0)])
		self.assertFalse((1,0) in next_generation)

if __name__ == '__main__':
	unittest.main()
