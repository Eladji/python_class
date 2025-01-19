import json
from classes.Fleet import Fleet
from classes.Marchand import Marchand
from classes.Mentalist import Mentalist
from classes.Operator import Operator
from classes.Pilote import Pilote
from classes.Armurier import Armurier
from classes.Spaceship import Spaceship
from classes.Technicien import Technicien
from classes.Entretien import Entretien

class FleetManager:
    def __init__(self, json_path='component/default.json'):
        self.current_fleet_index = 0
        self.test = "test"
        self.__metier_map = {
            "Pilote": Pilote,
            "Technicien": Technicien,
            "Armurier": Armurier,
            "Marchand": Marchand,
            "Entretien": Entretien
        }
        self.party = self.load_data(json_path)

    # @property
    # def _metier_map(self):
    #     return self.__metier_map

    # @_metier_map.setter
    # def _metier_map(self, value):
    #     self.__metier_map = value

    
    def load_data(self, json_path):
        with open(json_path, 'r') as file:
            datas = json.load(file)
        party = []
        for flotte_data in datas["Flottes"]:
            fleet = Fleet(flotte_data["Nom"])
            for vaisseau_data in flotte_data["Vaisseaux"]:
                ship = Spaceship(vaisseau_data["Nom"], vaisseau_data["Type"], [], vaisseau_data["Etat"])
                for crew in vaisseau_data["Equipage"]:
                    if crew["Type"] == "operator":
                        operator = Operator(crew["Prenom"], crew["Nom"], crew["Sexe"], crew["Age"], self.__metier_map.get(crew["Metier"])())
                        ship.append_member(operator)
                    elif crew["Type"] == "mentalist":
                        mentalist = Mentalist(crew["Prenom"], crew["Nom"], crew["Sexe"], crew["Age"], crew["Mana"])
                        ship.append_member(mentalist)
                fleet.append_spaceship(ship)
            party.append(fleet)
        return party
    
    def display_fleet_names(self):
        for fleet in self.party:
            print(fleet._name)
    
    def change_fleet(self, fleet_name):
        for index, fleet in enumerate(self.party):
            if fleet._name == fleet_name:
                self.current_fleet_index = index
                return True
        return False
    
    """
    without those function you need to repeat the same code in each function to find what you need in the party so yes but no
    """
    def get_current_fleet(self)-> Fleet:
        return self.party[self.current_fleet_index]
    
    def get_fleet_by_name(self, retries = 3)-> Fleet:
        if retries <= 0:
            print("Maximum retry limit reached. Exiting.")
            return None
        self.display_fleet_names()
        fleet_name = input("Nom de la flotte: \n")
        for fleet in self.party:
            if fleet._name == fleet_name:
                return fleet
        # If no fleet is found, print the message and return the current fleet
    def stat_party(self):
        for fleet in self.party:
            fleet.stat()
    
    def get_ship(self, current_fleet=None, retries=3) -> Spaceship:
    # Limit the recursion depth to avoid infinite loops
        if retries <= 0:
            print("Maximum retry limit reached. Exiting.")
            return None  # Return None or handle error
        
        if current_fleet is None:
            fleet = self.get_fleet_by_name()
            fleet.display_spaceship()
            input_ship = input("Nom du vaisseau: \n")
            for ship in fleet._spaceship:
                if ship._name == input_ship:
                    return ship
                
            print("couldn't find the wanted Spaceship")
            return self.get_ship(current_fleet=fleet, retries=retries-1)  # Retry with decremented counter
        else:
            self.get_current_fleet().display_spaceship()
            input_ship = input("Nom du vaisseau: \n")
            for ship in self.get_current_fleet()._spaceship:
                if ship._name == input_ship:
                    return ship
            print("couldn't find the wanted Spaceship")
            return self.get_ship(current_fleet=current_fleet, retries=retries-1)  # Retry with decremented counter

                
    def get_member(self, ship, retries=3):
        if retries <= 0:
            print("Maximum retry limit reached. Exiting.")
            return None
        ship.display_crew()
        input_member = input("Nom du membre: \n")
        for member in ship._crew:
            if member._first_name == input_member or member._last_name == input_member:
                return member
        print("couldn't find the wanted member")
        return self.get_member(ship, retries=retries-1)
    
    
    def show_menu(self):
        print("\n\t\tMenu\t\n")
        print(f"\tFlotte actuelle:\n\t {self.get_current_fleet()._name}\n")
        print("0 - afficher les stats de vos flottes")
        print("1 - ajouter une flotte")
        print("2 - suppression d'une flotte")
        print("3 - renommage d'une flotte")
        print("4 - Supprimer un membre de l'équipage")
        print("5 - Changement de flotte")
        print("6 - Ajouter un membre à l'équipage")
        print("7 - vérifier la préparation d'un vaisseau")
        print("8 - afficher l'équipage d'un vaisseau")
        print("9 - ajouter un vaisseau")
        print("10 - afficher les vaisseaux de la flotte")
        print("11 - Supprimer un vaisseau")
        print("12 - Quitter")
        return input("Votre choix: ")

    def input_handler(self):
        choice = self.show_menu()
        match choice:
            case "0":
                self.stat_party()
            case "1":
                self.add_fleet()
            case "2":
                fleet_name = input("Nom de la flotte: ")
                for fleet in self.party:
                    if fleet._name == fleet_name:
                        self.party.remove(fleet)
            case "3":
                self.rename_fleet()
            case "4":
                self.remove_member_from_ship()
            case "5":
                self.change_fleet_by_name()
            case "6":
                self.add_member_to_ship()
            case "7":
                self.check_preparation()
            case "8":
                self.get_ship(True).display_crew()
            case "9":
                self.add_ship_to_fleet()
            case "10":
                self.get_current_fleet().display_spaceship()
            case "11":
                self.remove_spaceship()
            case "12":
                exit(0)
            case _:
                print("Choix invalide")
    
    def remove_spaceship(self):
        ship = self.get_ship(True)
        self.get_current_fleet().remove_spaceship(ship)
    def check_preparation(self):
        ship = self.get_ship(True)
        check = ship.check_preparation()
        if check:
            print("Le vaisseau est prêt")
        else:
            print("Le vaisseau n'est pas prêt")
    
    def rename_fleet(self):
        fleet = self.get_current_fleet()
        new_name = input("Nouveau nom: ")
        if new_name == "" or len(new_name) <= 0 or len(new_name) > 20 or new_name in [fleet._name for fleet in self.party]:
            print("Nom invalide")
            return
        fleet._name = new_name
                
    def add_fleet(self):
        fleet_name = input("Nom de la flotte: ")
        self.party.append(Fleet(fleet_name))
        
    def add_ship_to_fleet(self):
        add_ship = input("Voulez-vous ajouter un vaisseau à une flotte existante ? (Oui, Non): ")
        if add_ship == "Non" or add_ship == "non" or add_ship == "N" or add_ship == "n":
            self.add_fleet()
            self.add_ship_to_fleet()
            self.change_fleet(self.party[-1]._name)
        fleet = self.get_current_fleet()
        ship_name = input("Nom du vaisseau: ")
        if ship_name == "" or len(ship_name) <= 0 or len(ship_name) > 20 or ship_name in [ship._name for ship in fleet._spaceship]:
            print("Nom invalide")
            return
        ship_type = input("Type de vaisseau (Transport ou Guerre): ")
        if ship_type != "Transport" or ship_type != "Guerre":
            return
        fleet.append_spaceship(Spaceship(ship_name, ship_type))
        
    def add_member_to_ship(self):
        ship = self.get_ship(True)
        input_last_name = input("Nom du membre: ")
        if input_last_name == "" or len(input_last_name) <= 0 or len(input_last_name) > 20 or input_last_name in [member._last_name for member in ship._crew]:
            print("Nom invalide")
            return
        input_first_name = input("Prénom du membre: ")
        if input_first_name == "" or len(input_first_name) <= 0 or len(input_first_name) > 20 or input_first_name in [member._first_name for member in ship._crew]:
            print("Prénom invalide")
            return
        input_age = int(input("Age du membre: "))
        if input_age <= 0 or input_age > 100:
            print("Age invalide")
            return
        input_gender = input("Sexe du membre (Homme, Femme): ")
        if input_gender != "Homme" and input_gender != "Femme" and input_gender != "H" and input_gender != "F":
            print("Sexe invalide")
            return
        if input_gender == "Homme" or input_gender == "H":
            input_gender = "Homme"
        if input_gender == "Femme " or input_gender == "F":
            input_gender = "Femme"
        input_Type = input("Type de membre (Operator, Mentalist): ")
        if input_Type == "Operator":
            input_role = input("Role du membre (Pilote, Technicien, Armurier, Marchand, Entretien): ")
            if input_role != "Pilote" and input_role != "Technicien" and input_role != "Armurier" and input_role != "Marchand" and input_role and "Entretien":
                print("Role invalide")
                return
            else:
                role_class = self.__metier_map.get(input_role)
                
                if role_class:
                    role_instance = role_class()
            new_member = Operator(input_first_name, input_last_name, input_gender, input_age, role_instance)
        if input_Type == "Mentalist":
            new_member = Mentalist(input_first_name, input_last_name, input_gender, input_age)
        if input_Type != "Mentalist" and input_Type != "Operator":
            print("Type de membre invalide")
            return
        ship.append_member(new_member)
                        
    def remove_member_from_ship(self):
        ship = self.get_ship(True)
        ship.display_crew()
        member = self.get_member(ship)
        if member:
            ship.remove_member(member)
        else:
            print("Membre invalide")

    def change_fleet_by_name(self):
        fleet = self.get_fleet_by_name()
        if not self.change_fleet(fleet._name):
            print("Flotte inexistante")

    def run(self):
        while True:
            self.input_handler()


# Instantiate FleetManager and run
if __name__ == "__main__":
    fleet_manager = FleetManager()
    fleet_manager.run()
