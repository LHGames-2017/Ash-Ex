
from actions import *

def createPath(oldPos, newPos):
	pass
	return newPos


def moveToLocation(oldPos, newPos):
	path = createPath(oldPos, newPos)
	for position in path:
		create_move_action(position)

def isFull(player):
	return (player.CarriedRessources == player.CarryingCapacity)

def returnHome(player):
	moveToLocation(player.Position, player.HouseLocation)

def isSomeoneCloseToHome():
	pass

def gatherResources(player):
	if isFull(player):
		returnHome(player)
	else:
		pass
		### TODO: code it
		
