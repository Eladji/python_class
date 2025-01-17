class Technicien():
    def __init__(self, rep_ship= True, drive_ship = False):
        super().__init__(rep_ship, drive_ship)
    def act(self):
        print("Répare le vaisseau\n")