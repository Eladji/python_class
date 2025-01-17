from classes.Fleet import Fleet
from classes.Marchand import Marchand
from classes.Mentalist import Mentalist
from classes.Operator import Operator
from classes.Pilote import Pilote
from classes.Armurier import Armurier
from classes.Spaceship import Spaceship
from classes.Technicien import Technicien
from classes.Entretien import Entretien
import json

def init():
    with open('component/default.json','r') as file:
            datas = json.load(file)
    metier_map = {
        "Pilote": Pilote,
        "Technicien": Technicien,
        "Armurier": Armurier,
        "Marchand": Marchand,
        "Entretien": Entretien
    }
    for data in datas["Vaisseaux"]:
        fleet = Fleet(datas["Flotte"]["Nom"])
        ship = Spaceship(data["Nom"], data["Type"], [], data["Etat"])
        for crew in data["Equipage"]:
            if crew["Type"] == "operator":
                role_class = metier_map.get(crew["Metier"])
                if role_class:
                    role_instance = role_class()
                    operator = Operator(crew["Nom"], crew["Nom"], crew["Sexe"], crew["Age"], role_instance)
                    ship.append_member(operator)
            elif crew["Type"] == "mentalist":
                mentalist = Mentalist(crew["Nom"], crew["Nom"], crew["Sexe"], crew["Age"], crew["Mana"])
                ship.append_member(mentalist)
        fleet.append_spaceship(ship)
    return fleet

def main():
    fleet = init()
    fleet.stat()
    
if __name__ == "__main__":
    main()  
