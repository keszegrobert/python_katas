class GameOfLife:
	def evolve(self,cells):
		next_generation = set()
		for cell in cells:
			neighbourcount = self.__count_living_neighbours(cell,cells)
			if neighbourcount == 2 or neighbourcount == 3:
				next_generation.add(cell)
			for neighbour in self.__get_neighbours(cell):
				if neighbour not in cells and \
					self.__count_living_neighbours(neighbour,cells) == 3:
					next_generation.add(neighbour)

		return next_generation

	def __get_neighbours(self,cell):
		neighbours = []
		x,y = cell
		for dx,dy in self.__get_neighbour_offsets():
			neighbour = (x+dx,y+dy)
			neighbours.append(neighbour)
		return neighbours

	def __count_living_neighbours(self,cell,cells):
		number_of_neighbours = 0
		x,y = cell
		for neighbour in self.__get_neighbours(cell):
			if neighbour in cells:
				number_of_neighbours += 1
		return number_of_neighbours

	def __get_neighbour_offsets(self):
		return [(-1,-1),(-1,0),(-1,1),
				( 0,-1),       ( 0,1),
				( 1,-1),( 1,0),( 1,1)]

