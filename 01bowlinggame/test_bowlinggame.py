from bowlinggame import BowlingGame
from nose.tools import with_setup

game = None

#https://github.com/hontas/bowling-game-kata
def setup_func():
	global game
	game = BowlingGame()

def teardown_func():
	pass

@with_setup(setup_func,teardown_func)
def test_guttergame():
	global game
	for i in range(0,20):
		game.roll(0)
	assert game.score() == 0

@with_setup(setup_func,teardown_func)
def test_gameofones():
	global game
	for i in range(0,20):
		game.roll(1)
	assert game.score() == 20
