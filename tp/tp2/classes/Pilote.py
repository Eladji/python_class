import Role
class Pilote(Role):
    def __init__(self, rep_ship= False, drive_ship = True):
        super().__init__(rep_ship, drive_ship)
    
    def act(self):
        print("Pilote le vaisseau\n")