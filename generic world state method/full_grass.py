def create_state(world_size):
	world_state = []
	for _ in range(world_size):
		row = []
		for _ in range(world_size):
			row.append(Entities.Grass)
		world_state.append(row)
	return world_state