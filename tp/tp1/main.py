
import json
import random
from crewmember import CrewMember

count = 0
def init():
    member = CrewMember().load()
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
            CrewMember.save()
            exit()
        case _:
            print("invalid choice")
    count += 1 
    if count == 5:
        print("un evenement a eu lieu")
        event = random.randint(0, 5)
        match event:
            case 0:
                print("un membre est mort")
                CrewMember.removefromlist(random.randint(0, len(CrewMember.crewlist)))
            case 1:
                print("un membre a gagné de l'expérience")
                CrewMember.crewlist[random.randint(0, len(CrewMember.crewlist))].gainxp()
            case 2:
                print(" un membre a perdu de l'expérience")
                CrewMember.crewlist[random.randint(0, len(CrewMember.crewlist))].losexp()
            case 3:
                print("un membre a gagné de la mana")
                CrewMember.crewlist[random.randint(0, len(CrewMember.crewlist))].gainmana()
            case 4:
                print("un membre a perdu de la mana")
                CrewMember.crewlist[random.randint(0, len(CrewMember.crewlist))].losemana()
            case 5:
                print("il ne c'est rien passé")
        count = 0
if __name__ == "__main__":
    init()
    while True:
        main()