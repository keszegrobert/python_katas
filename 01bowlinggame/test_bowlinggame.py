from bowlinggame import BowlingGame

#https://github.com/hontas/bowling-game-kata

def test_guttergame():
	game = BowlingGame()
	game.roll(0)
	assert game.score() == 0