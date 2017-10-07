from structs import *


def findThings(dMap, content):
    tilesFound = []
    for tiles in dMap:
        for tile in tiles:  
            if tile.Content in content: 
                tilesFound.append(tile)

    return tilesFound


def obstaclesToWalls(obstacles):
    wallA = []
    for obstacle in obstacles:
        wallA.append((obstacle.X, obstacle.Y))

    return wallA

def fillWeights():
    weights = {}
    for y in range(40):
        for x in range(40):
            weights[(x,y)] = 1

    return weights
