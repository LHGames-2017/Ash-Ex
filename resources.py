
from actions import *
from implementation import *

def createPath(grid, start, goal):
	startT = (start.X,start.Y)
	goalT  = (goal.X,goal.Y)
	came_from, cost_so_far = a_star_search(grid, startT, goalT)
	path = list(reversed(reconstruct_path(came_from,start=startT,goal=goalT)))

	return path

def moveToLocation(oldPos, newPos):
	pass
	#path = createPath(oldPos, newPos)
	#for position in path:
	#	create_move_action(position)

def isFull(player):
	if player.CarriedRessources < player.CarryingCapacity:
		return False
	return True

def returnHome(player):
	moveToLocation(player.Position, player.HouseLocation)

def gatherResources(player):
	if isFull(player):
		returnHome(player)
		gatherResources(player)
	else:
		pass
		### TODO: code it
		
