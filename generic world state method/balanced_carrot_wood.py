def create_state(world_size):
	world_state = [] # represents world state from bottom to top, left to right
	# create checkerboard of carrots and trees by appending tree if both x and y 
	# are even or odd, otherwise append carrot
	for y in range(world_size-1):
		row = []
		for x in range(world_size):
			if (y % 2) == 0:
				if (x % 2) == 0:
					row.append(Entities.Tree)
				else:
					row.append(Entities.Carrot)
			else:
				if (x % 2) == 0:
					row.append(Entities.Carrot)
				else:
					row.append(Entities.Tree)
		world_state.append(row)
	row = []
	for x in range(world_size):
		row.append(Entities.Grass)
	world_state.append(row)
	return world_state