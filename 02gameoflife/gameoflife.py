class GameOfLife:
	def evolve(self,cells):
		next_generation = set()
		for cell in cells:
			neighbourcount = self.__count_living_neighbours(cell)
			if neighbourcount == 2 or neighbourcount == 3:
				next_generation.add(cell)
		return next_generation

	def __count_living_neighbours(self,cell):
		x,y = cell
		return x + y
