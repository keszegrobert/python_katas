class GameOfLife:
	def evolve(self,cells):
		next_generation = set()
		for cell in cells:
			neighbourcount = self.__count_living_neighbours(cell,cells)
			if neighbourcount == 2 or neighbourcount == 3:
				next_generation.add(cell)
		return next_generation

	def __count_living_neighbours(self,cell,cells):
		numbber_of_neighbours = 0
		x,y = cell
		for (dx,dy) in [(-1,-1),(-1,0),(-1,1),
						( 0,-1),       ( 0,1),
						( 1,-1),( 1,0),( 1,1)]:
			neighbour = (x+dx,y+dy)
			if (neighbour in cells):
				numbber_of_neighbours += 1	
		return numbber_of_neighbours
