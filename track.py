
def leveledUp(oldMaxHealth, newMaxHealth):
	if oldMaxHealth != newMaxHealth:
		return True
	return False

def findClosetObject(position, objects):
	currentDistance = 1600
	for obj in objects:
		newDistance = abs(obj.X - position.X) + abs(obj.Y - position.Y)
		if newDistance < currentDistance:
			currentDistance = newDistance
			newPosition = obj
	return newPosition


def playerHouse(playerInfo, houses):
	if playerInfo.house == None and playerInfo.oldHealth != None:
		if playerInfo.MaxHealth != playerInfo.oldHealth:
			position = findClosetObject(playerInfo.position, houses)
			return position

	return playerInfo.House