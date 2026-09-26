def move_to(x, y):
	world_size = get_world_size()
	quick_print("moving to: (" + str(x) + ", " + str(y) + ")")
	deltax = get_pos_x() - x # can caluclate beforehand as direction doesn't change
	while (get_pos_x() != x):
		# shortest path considering wraparounds
		if (deltax >= 0 and deltax <= world_size/2) or (deltax < -world_size/2):
			move(West)
		else: # current_x > target_x:
			move(East)
	deltay = get_pos_y() - y
	while (get_pos_y() != y):
		if (deltay >= 0 and deltay <= world_size/2) or (deltay < -world_size/2):
			move(South)
		else: # current_x > target_x:
			move(North)
	#debug
	#print("at (" + str(get_pos_x()) + ", " + str(get_pos_y()) + ")")

def reset_position():
	move_to(0, 0)