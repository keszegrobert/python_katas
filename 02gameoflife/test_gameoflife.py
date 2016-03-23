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


	def test_if_any_cell_with_two_or_three_neighbours_survives(self):
		self.evolve([      (1,1),(2,1),
			         (0,2),(1,2)])
		self.assert_alive((0,2))
		self.assert_alive((1,2))

	def evolve(self,cells):
		self.next_generation = self.game.evolve(cells)

	def assert_dead(self,cell):
		self.assertFalse(cell in self.next_generation)

	def assert_alive(self,cell):
		self.assertTrue(cell in self.next_generation)

if __name__ == '__main__':
	unittest.main()
