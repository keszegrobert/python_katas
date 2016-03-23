class GameOfLife:
	def evolve(self,cells):
		next_generation = set()
		for (x,y) in cells:
			neighbourcount = x+y
			if neighbourcount == 2 or neighbourcount == 3:
				next_generation.add((x,y))
		return next_generation
