
import json
from crewmember import CrewMember
def init():
    with open('default.json','r') as file:
            data = json.load(file)
    for crewmem in data["Foundation"]["CrewMembers"]["Operators"]:
        member = CrewMember().autoinit(crewmem["FirstName"], crewmem["LastName"], crewmem["Age"], crewmem["Gender"], crewmem["Job"], "Operator", 0)
        member.addtolist()

    for crewmem in data["Foundation"]["CrewMembers"]["Mentalists"]:
        member = CrewMember().autoinit(crewmem["FirstName"], crewmem["LastName"], crewmem["Age"], crewmem["Gender"], "Mentalist", crewmem["Mana"])
        member.addtolist()

print("Bienvenue dans votre gestionnaire de flotte")
def main():
    choice = int(input("\n[1]. ajouter un membre a une flotte\n [2]. enlever un membre a une flotte\n [3] afficher les membre\n [4]. Exit\n"))
    match choice:
        case 1:
            
            member =CrewMember().new()
            member.addtolist()
         
            
        case 2:
            CrewMember.displaylist()
            member =CrewMember.selectfromlist(int(input("indiquer le nom du membre")))
            CrewMember.removefromlist(member)
        case 3:
            CrewMember.displaylist()
        case 4:
            exit()
        case _:
            print("invalid choice")

if __name__ == "__main__":
    init()
    while True:
        main()