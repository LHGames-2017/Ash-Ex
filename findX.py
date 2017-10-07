from structs import *
import json
import numpy as np



def findThings(dMap, content):
    tilesFound = []
    for tiles in dMap:
        for tile in tiles: 
            if tile.Content == content:
                tilesFound.append(tile)
    return tilesFound