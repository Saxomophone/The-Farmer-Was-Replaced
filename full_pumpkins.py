import motion
def pumpkins(world_size):
	first_loop = True
	while True:
		#check if sufficient carrot supply
		
		incomplete_tiles = []
		# plant pumpkins everywhere. assumes you have sufficient carrots
		for y in range(world_size):
			for x in range(world_size):
				if first_loop:
					till()
				plant(Entities.Pumpkin)
				incomplete_tiles.append((x, y))
				move(North)
			move(East)
			
		for x, y in incomplete_tiles:
			motion.move_to(x, y)
			if not can_harvest():
				if (get_entity_type() == Entities.Dead_Pumpkin):
					plant(Entities.Pumpkin)
				incomplete_tiles.append((x,y))
						
		motion.move_to(0, 0)
		harvest()
		first_loop = False
			
			
			