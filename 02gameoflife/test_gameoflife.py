from unittest import TestCase
from gameoflife import GameOfLife

class TestGameOfLife(TestCase):
	def test_if_gameoflife_can_be_instantiated(self):
		game = GameOfLife()

if __name__ == '__main__':
	unittest.main()
