
from actions import *

def createPath(oldPos, newPos):
	pass
	return newPos

def moveToLocation(oldPos, newPos):
	path = createPath(oldPos, newPos)
	for position in path:
		create_move_action(position)

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
		
