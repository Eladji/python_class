from classes.FleetManager import FleetManager
from classes.GUI import GUI

    
if __name__ == "__main__": 
    input = input("Voulez-vous lancer le jeu avec interface (O/N) : ")
    if input == "O":
        GUI = GUI()
        GUI.run()   
    else:
        game = FleetManager()
        game.run()    