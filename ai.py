from flask import Flask, request
from structs import *
import json
import numpy as np

from utilsD import *
from implementation import *
from resources import *


app = Flask(__name__)


grid = GridWithWeights(40,40)
grid.weights = fillWeights()

path = []

def bot():
    """
    Main de votre bot.
    """
    global grid
    global path

    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map)
    p = map_json["Player"]
    #print("player:{}".format(p))
    pos = p["Position"]
    x = pos["X"]
    y = pos["Y"]
    house = p["HouseLocation"]
    player = Player(p["Health"], p["MaxHealth"], Point(x,y),
                    Point(house["X"], house["Y"]), p["Score"],
                    p["CarriedResources"], p["CarryingCapacity"])

    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)

    otherPlayers = []

    for players in map_json["OtherPlayers"]:
        player_info = players["Value"]
        p_pos = player_info["Position"]
        player_info = PlayerInfo(player_info["Health"],
                                player_info["MaxHealth"],
                                Point(p_pos["X"], p_pos["Y"]))

        otherPlayers.append(player_info)

    #########  TESTING  ########
    lavas = findThings(deserialized_map, TileContent.Lava)
    walls = findThings(deserialized_map, TileContent.Wall)
    grid.walls = obstaclesToWalls(lavas, walls)

    #######################

    #print()
    #draw_grid(grid,width=3, number=cost_so_far, start=(x,y),goal=(11,10))
    #print()
    #draw_grid(grid, width=3, path=reconstruct_path(came_from, start=(x,y), goal=(11, 10)))

    print(player.Position)
    pi = Point(x,y)
    pg = Point(11,10)
    path = createPath(grid,pi,pg)
    for lava in lavas:
        print(lava.X, lava.Y)
    print(path)
    return moveToLocation(path) 

    input()

@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)