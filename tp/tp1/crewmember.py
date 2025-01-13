import json
from pathlib import Path
crewlist = []
class CrewMember:
    def new(self):
        self.Lastname = input("enter le nom du membre\n")         
        self.firstname= input("enter le prenom du membre\n")
        self.age:int =  input("entrer l'age du membre\n")
        self.job:str = self.choosejob()
        self.gender:bool = input("entrer 1. pour homme et 0. pour femme\n")
        self.type:str = self.choosetype()
        self.Mana:int = input("indiquer le mana du membre\n")
        return self
    
    def autoinit(self, firstname:str, Lastname, age:int, gender:str,  job:str, type:str, Mana:int=None):
        
        self.Lastname = Lastname
        self.firstname:str = firstname
        self.age:int = age
        self.job:str = job
        self.gender:str = gender
        self.type:str = type
        self.Mana:int = Mana
        self.xp:int = 0
        return self
    def gainxp(self):
        self.xp += 1
        return
    def losexp(self):
        self.xp -= 1
        return
    def gainmana(self):
        self.Mana += 1
        return
    def losmana(self):
        self.Mana -= 1
        return
    def save(self):
        with open('crew.json','w') as file:
            json.dump(self.__dict__, file)
        return
    def load(self):
        my_file = Path("crew.json")
        if my_file.is_file():
            with open('crew.json','r') as file:
                data = json.load(file)
            self.__dict__ = data
        return
    def __str__(self)->str:
        return f" {self.Lastname} {self.firstname}, {self.age} ans un {self.job}\n"

    def job(self)->str:
        match self.job:
            case 0:
                return "Commandant"
            case 1:
                return "Pilote"
            case 2:
                return "Marchand"
            case 3:
                return "Armurier"
            case 4:
                return "Entretien"
            case 5:
                return "Technicien"
            case _:
                return "this crew member is jobless"

    def choosejob(self)->str:
        with open('default.json','r') as file:
            data = json.load(file)
        print("choissisez le métier du membre")
        i=0
        for key in data["Foundation"]["CrewMembers"]["Jobs"]:
            print(f"{i}.{key}") 
            i+=1 
            match input():
                case 0:
                     
                    return "Commandant"
                case 1:
                     
                    return "Pilote"
                case 2:
                     
                    return "Marchand"
                case 3:
                     
                    return "Armurier"
                case 4:
                     
                    return "Entretien"
                case 5:
                     
                    return "Technicien"
                case _:
                     
                    return "invalid choice"
            
    def choosetype(self)->str:
        with open('default.json','r') as file:
            data = json.load(file)
        print("choissisez le type de membre")
        i=0
        for key in data["Foundation"]["CrewMembers"]["Types"]:
            print(f"{i}.{key}") 
            i+=1 
            match input():
                case 0:
                    return "Opérateur"
                case 1:
                    return "Mentalistes"
                case _:
                    return "invalid choice"
    def addtolist(self):
        crewlist.append(self)
        return crewlist
    def removefromlist(id:int):
        crewlist.remove(id)
        return crewlist
    def displaylist():
        i= 0
        for member in crewlist:
            print(f"{i}.{member}\n")
            i+=1
        return None
    def selectfromlist(id:int):
        return crewlist[id]