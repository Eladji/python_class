from crewmember import CrewMember
crewList = []
class Crew:
    def __init__(self, ship:list = None, name:str = None, crewlist:list = None, commandant:CrewMember = None):
        self.name = input("enter the name of the crew")
        self.cremember = crewlist
        self.commandant = CrewMember
        self.ship = ship
        crewList.append(self)

    def addcrew(self, CrewMember:object):
        
        self.cremember.append(CrewMember)

    def display_crew(self):
        for member in self.cremember:
            print(member.name)
    
    def check(self):
        if len(self.crewlist) == 0:
            print("the crew is empty")
        else:
            print("the crew is not empty")
    
    def remove(self, member:CrewMember):
        self.cremember.remove(member)
    def addcrewl(self, CrewMember):
        
        crewlist.append(self)
    
    def removefromlist(id:int, crewlist:list):
        crewlist.remove(id)
        return crewlist
    def selectfromlist(self, name:str):
        for member in self.crewlist:
            if member.name == name:
                return member
        print("no such member")
        return None