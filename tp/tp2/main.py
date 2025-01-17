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
    with open('component/default.json', 'r') as file:
        datas = json.load(file)
    party = []
    metier_map = {
        "Pilote": Pilote,
        "Technicien": Technicien,
        "Armurier": Armurier,
        "Marchand": Marchand,
        "Entretien": Entretien
    }
    for flotte_data in datas["Flottes"]:
        fleet = Fleet(flotte_data["Nom"])
        for vaisseau_data in flotte_data["Vaisseaux"]:
            ship = Spaceship(vaisseau_data["Nom"], vaisseau_data["Type"], [], vaisseau_data["Etat"])
            for crew in vaisseau_data["Equipage"]:
                if crew["Type"] == "operator":
                    role_class = metier_map.get(crew["Metier"])
                    if role_class:
                        role_instance = role_class()
                        operator = Operator(crew["Prenom"], crew["Nom"], crew["Sexe"], crew["Age"], role_instance)
                        ship.append_member(operator)
                elif crew["Type"] == "mentalist":
                    mentalist = Mentalist(crew["Prenom"], crew["Nom"], crew["Sexe"], crew["Age"], crew["Mana"])
                    ship.append_member(mentalist)
            fleet.append_spaceship(ship)
        party.append(fleet)
    return party

def main():
    party = init()
    for f in party:
        f.stat()
    
if __name__ == "__main__":
    main()  
