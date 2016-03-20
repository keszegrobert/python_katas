from bowlinggame import BowlingGame

#https://github.com/hontas/bowling-game-kata

def test_guttergame():
	game = BowlingGame()
	for i in range(1,20):
		game.roll(0)
	assert game.score() == 0

def test_gameofones():
	game = BowlingGame()
	for i in range(0,20):
		game.roll(1)
	assert game.score() == 20