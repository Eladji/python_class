from classes import *
import json

def init():
    with open('component/default.json','r') as file:
            datas = json.load(file)
    for data in datas["Flotte"]:
        float = Fleet(data["name"])
        for ship in data["spaceship"]:
            shid = Ship(ship["name"], ship["Type"], ship["Equipage"], ship["state"])
            Fleet.append_spaceship(ship)
