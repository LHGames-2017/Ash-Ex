from structs import *


def findThings(dMap, content):
    tilesFound = []
    for tiles in dMap:
        for tile in tiles:  
            if tile.Content == content: 
                tilesFound.append(tile)

    return tilesFound


def obstaclesToWalls(lavas, walls, otherPlayers):
    tilesFound = walls + lavas
    wallA = []
    for obstacle in tilesFound:
        wallA.append((obstacle.X, obstacle.Y))

    for player in otherPlayers:
        pos = player.Position
        wallA.append((pos.X,pos.Y))
    
    return wallA