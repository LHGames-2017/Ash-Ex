from structs import *


def findThings(dMap, content):
    tilesFound = []
    for tiles in dMap:
        for tile in tiles:  
            if tile.Content == content: 
                tilesFound.append(tile)

    return tilesFound


def tilesToWalls(lavas, walls):
    tilesFound = walls + lavas
    wallA = []
    for obstacle in tilesFound:
        wallA.append((obstacle.X, obstacle.Y))
    print(wallA)
    return wallA