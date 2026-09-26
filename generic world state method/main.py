from balanced_carrot_wood import create_state
import motion
import optimal_pumpkins
import tillage


def till_world(world_state):
	for y in world_state:
		for x in y:
			if x in soil_crops:
				till()
			move(North)
		move(East)
			
def loop(world_state):
	while True:
		for y in world_state:
			for x in y:
				if can_harvest() or get_entity_type() in replant:
					harvest()
					plant(x)
				water(x)
				move(North)
			move(East)
					
					
				

def water(current_crop):
	if current_crop in prioritised_crops_water:
		if get_water() < 0.8:
			use_item(Items.Water)
	


world_size = get_world_size()
soil_crops = [Entities.Carrot, Entities.Pumpkin]
grassland_crops = [Entities.Grass, Entities.Bush, Entities.Tree]
prioritised_crops_water = []
replant = [Entities.Dead_Pumpkin, None, Entities.Grass]

clear()
#optimal_pumpkins.pumpkins(world_size)
world_state = create_state(world_size)
till_world(world_state)
loop(world_state)