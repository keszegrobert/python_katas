from unittest import TestCase
from gameoflife import GameOfLife

class TestGameOfLife(TestCase):
	def setUp(self):
		self.game = GameOfLife()

	def test_if_any_cell_with_less_than_two_neighbours_dies(self):
		self.evolve([(0,0)])
		self.assert_dead((0,0))
		self.evolve([(0,0),(1,0)])
		self.assert_dead((1,0))

	def evolve(self,cells):
		self.next_generation = self.game.evolve(cells)

	def assert_dead(self,cell):
		self.assertFalse(cell in self.next_generation)

if __name__ == '__main__':
	unittest.main()
