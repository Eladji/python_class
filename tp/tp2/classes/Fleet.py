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
                        nbt_xp += member._xp()
                        match type(member._role()).__name__:
                            case 'Pilote':
                                nbt_p += 1
                            case 'Technicien':
                                nbt_t += 1
                    case 'Mentalist':
                        nbt_M +=1                  
            nbt_O += (nbt_p + nbt_t)
            nbt += nbt_O  + nbt_M
        print(f"\n Voici les Stats de la flotte:\n_____\nNombre de membres :\n    {nbt} \n    - {nbt_O} Operateurs\n      - {nbt_p} Pilotes\n     - {nbt_t} Techniciens\n - {nbt_M} Mentalistes\n_____\nExpérience:\n   - {nbt_xp} d'xp total\n - {nbt_xp/nbt} d'xp moyenne\n")