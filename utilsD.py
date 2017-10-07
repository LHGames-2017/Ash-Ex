from structs import *


def findThings(dMap, content):
    tilesFound = []
    for tiles in dMap:
        for tile in tiles:  
            if tile.Content == content: 
                tilesFound.append(tile)

    return tilesFound


def obstaclesToWalls(lavas, walls):
    tilesFound = walls + lavas
    wallA = []
    for obstacle in tilesFound:
        wallA.append((obstacle.X, obstacle.Y))

    return wallA

def fillWeights():
    weights = {}
    for y in range(40):
        for x in range(40):
            weights[(x,y)] = 1

    return weights
