from flask import Flask, request
from structs import *
import json
import numpy as np

from utilsD import *
from astar.implementation import *
from resources import *


app = Flask(__name__)

def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """
    serialized_map = serialized_map[1:]
    rows = serialized_map.split('[')
    column = rows[0].split('{')
    deserialized_map = [[Tile() for x in range(40)] for y in range(40)]
    for i in range(len(rows) - 1):
        column = rows[i + 1].split('{')

        for j in range(len(column) - 1):
            infos = column[j + 1].split(',')
            end_index = infos[2].find('}')
            content = int(infos[0])
            x = int(infos[1])
            y = int(infos[2][:end_index])
            deserialized_map[i][j] = Tile(content, x, y)

    return deserialized_map



def bot():
    """
    Main de votre bot.
    """
    grid = SquareGrid(40,40)


    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map)
    p = map_json["Player"]
    pos = p["Position"]
    x = pos["X"]
    y = pos["Y"]
    house = p["HouseLocation"]
    player = Player(p["Health"], p["MaxHealth"], Point(x,y),
                    Point(house["X"], house["Y"]),
                    p["CarriedResources"], p["CarryingCapacity"])

    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)

    otherPlayers = []

    for player_dict in map_json["OtherPlayers"]:
        for player_name in player_dict.keys():
            player_info = player_dict[player_name]
            if player_info == 'notAPlayer':
                continue
            p_pos = player_info["Position"]
            player_info = PlayerInfo(player_info["Health"],
                                   player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

            otherPlayers.append({player_name: player_info })
    # return decision

    #########  TESTING  ########
    lavas = findThings(deserialized_map, TileContent.Lava)
    walls = findThings(deserialized_map, TileContent.Wall)
    grid.walls = obstaclesToWalls(lavas, walls, otherPlayers)

    #######################


    came_from, cost_so_far = a_star_search(grid, (x,y),(11,10))

    draw_grid(grid)
   # print(otherPlayers[0]["Value"].Position)
    print(pos)
    return create_move_action(Point(x, y))
    print(findThings(deserialized_map, TileContent.Lava))
    input()

    return create_move_action(Point(x-1, y))

@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)