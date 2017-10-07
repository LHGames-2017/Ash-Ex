
from actions import *
from implementation import *

def createPath(grid, start, goal):
	startT = (start.X,start.Y)
	goalT  = (goal.X,goal.Y)
	came_from, cost_so_far = a_star_search(grid, startT, goalT)
	path = list(reversed(reconstruct_path(came_from,start=startT,goal=goalT)))[:-2]

	return path

def convertTuplePoint(tuple):
	return Point(tuple[0], tuple[1])

def followPath(path):
	pos = convertTuplePoint(path.pop())
	return create_move_action(pos)

def isFull(player):
	return (player.CarriedRessources == player.CarryingCapacity)

def isSomeoneCloseToHome():
	pass