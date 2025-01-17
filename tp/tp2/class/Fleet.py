import Ship 
class Fleet():
    def __init__(self, name, spaceship = []):
        self.__name = name
        self.__spaceship = spaceship

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _spaceship(self):
        return self.__spaceship

    def append_spaceship(self, Ship):
        self.__spaceship.append(Ship)
        print(f"{Ship._name()} a rejoint la flotte")
 
    def remove_spaceship(self, value):
        self.__spaceship.pop(value._name())
        print(f"{value._name()} a quitter la flotte")

    def stat(self):
        for ship in self.__spaceship:
            for member in ship:
                match type(member).__name__:
                    case 'Operator':
                        match type(member._role()).__name__:
                            case 'Pilote':
                                nbt_p += 1
                            case 'Technicien':
                                nbt_t += 1
                    case 'Mentalist':
                        nbt_M +=1
                    
                    case _:
            nbt += ship._crew().size()

        print(f"\n Voici les Stats de la flotte:\n nombre de membres :\n    
